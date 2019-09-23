import java.io.IOException;
import java.util.Date;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;

public class TestDynamic {

    public static String authHeader(String orderno, String secret, int timestamp){
		//拼装签名字符串
		String planText = String.format("orderno=%s,secret=%s,timestamp=%d", orderno, secret, timestamp);

		//计算签名
		String sign = org.apache.commons.codec.digest.DigestUtils.md5Hex(planText).toUpperCase();

		//拼装请求头Proxy-Authorization的值
		String authHeader = String.format("sign=%s&orderno=%s&timestamp=%d", sign, orderno, timestamp);
		return authHeader;
	}

	public static void main(String[] args) throws IOException {
        final String url = "http://2000019.ip138.com";

		final String ip = "forward.xdaili.cn";//这里以正式服务器ip地址为准
		final int port = 80;//这里以正式服务器端口地址为准

		int timestamp = (int) (new Date().getTime()/1000);
		//以下订单号，secret参数 须自行改动
		final String authHeader = authHeader("ZF2017974xxxxxxx", "cb65091847adxxxxxxxxxxxx", timestamp);
		int count = 5;
		ExecutorService thread = Executors.newFixedThreadPool(count);

		for (int i=0;i<count;i++) {
			Task task = new Task(url, ip, port, authHeader);
			thread.execute(task);
		}
		thread.shutdown();
	}

	static class Task extends Thread {

		private String url;
		private String ip;
		private int port;
		private String authHeader;

		public Task(String url, String ip, int port, String authHeader) {
			this.url = url;
			this.ip = ip;
			this.port = port;
			this.authHeader = authHeader;
		}

		@Override
		public void run() {
			Long startTime = System.currentTimeMillis();
			Document doc = null ;
			try {
				doc = Jsoup.connect(url)
						.proxy(ip, port)
						.validateTLSCertificates(false) //忽略证书认证,每种语言客户端都有类似的API
						.header("Proxy-Authorization", authHeader)
						.get();

	                    System.out.println(" 返回结果:"+doc.outerHtml() );
//				System.out.println(String.format("%s 用时 %s毫秒", this.getName(), System.currentTimeMillis() - startTime));
			} catch (Exception e) {
				System.out.println(String.format("%s 超时", this.getName()));
				e.printStackTrace();
			}
		}
	}
        
}
