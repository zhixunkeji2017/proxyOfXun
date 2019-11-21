import org.apache.http.HttpResponse;
import org.apache.http.client.config.RequestConfig;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.concurrent.FutureCallback;
import org.apache.http.impl.nio.client.CloseableHttpAsyncClient;
import org.apache.http.impl.nio.client.HttpAsyncClients;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.UnsupportedEncodingException;
import java.security.NoSuchAlgorithmException;
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.Future;
/**
 * 拨号示例
 * @author Administrator
 *
 */
public class GetDynamicIP {
    //url规则为http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP/{orderno}/{proxyId}
    private static String url = "http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP/DD201911218432z9iG9s/433a83d2f96d12e9af127cd30abda612";

    public static void main(String[] args) throws NoSuchAlgorithmException, UnsupportedEncodingException {
        HttpGet get = new HttpGet(url);
        RequestConfig requestConfig = RequestConfig.custom().setSocketTimeout(150000).setConnectTimeout(150000).build();
        CloseableHttpAsyncClient httpclient = HttpAsyncClients.custom().setDefaultRequestConfig(requestConfig).build();
        try {
            httpclient.start();
            final CountDownLatch latch = new CountDownLatch(1);
            final StringBuilder result = new StringBuilder();
            Future<HttpResponse> future = httpclient.execute(get, new FutureCallback<HttpResponse>() {
                @Override
                public void completed(final HttpResponse response) {
                    BufferedReader reader = null;
                    try {
                        reader = new BufferedReader(new InputStreamReader(response.getEntity().getContent()));

                        String line = null;
                        while ((line = reader.readLine()) != null) {
                            result.append(line + "\n");
                        }
                        System.out.println(result);
                    } catch (IOException e) {
                    } finally {
                        try {
                            reader.close();
                        } catch (IOException e) {
                        }
                    }
                    latch.countDown();
                }

                @Override
                public void failed(final Exception ex) {
                    latch.countDown();
                }

                @Override
                public void cancelled() {
                    latch.countDown();
                }

            });
            latch.await();
        } catch (Exception e) {
        } finally {
            try {
                httpclient.close();
            } catch (IOException e) {

            }
        }

    }
}
