	public function immediate(){
		$time = time();
		$orderno = xxx;
		$secret = xxx;

		$planText="orderno=".$orderno.",secret=".$secret.",timestamp=".$time;
		$sign = strtoupper(md5($planText));
		$auth = 'sign='.$sign.'&orderno='.$orderno.'&timestamp='.$time;
		$url = xxx;
        $ch = curl_init();
        // 设置浏览器的特定header
        curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        	"Proxy-Authorization:".$auth,
	        "Connection: keep-alive",
	        "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
	        "Upgrade-Insecure-Requests: 1",
	        "DNT:1",
	        "Accept-Language: zh-CN,zh;q=0.8,en-GB;q=0.6,en;q=0.4,en-US;q=0.2",
	        'Cookie:x-wl-uid=13+U2muoAsqb+cGICuLwsZxdB0zh3Cxftc3w0L1osYFaHBsx69LBKo+Ye1VlRE6mQYAJdfOz/pCU=; session-token=VCkyOjvA47ITaveT83S7oYA8fykTsO+1DRP99i+7pYoZS6t1O5Rc2grgfX7v1MQsvcTcd04UoSNd2LxjUFw7KoAuVTbq8i1U4CuJqn8xGyP71O7MeEOXbGOov6s3dgcaDBObgk7TEq6l+9LulY9sk/ddoh5sJXeZCJCDdv5ui9Dx6FDNQQoGI6jS/i/mWQLH5jUYgCfwRZgWLb/LYt4RzXrAUaldRJPhfwK0fVNuCZt1ZpexTddfMxnzeq5+gmRB; csm-hit=s-673XVDH32ASPKJC03C10|1499052510486; ubid-main=134-1565384-9955147; session-id-time=2082787201l; session-id=144-7849927-7600125',
			));
		
		curl_setopt($ch, CURLOPT_USERAGENT, 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11');
	    curl_setopt($ch, CURLOPT_REFERER,"https://www.baidu.com/s?word=%E7%9F%A5%E4%B9%8E&tn=sitehao123&ie=utf-8&ssl_sample=normal&f=3&rsp=0");
	    curl_setopt($ch, CURLOPT_ENCODING, "gzip, deflate, sdch");
	    curl_setopt($ch, CURLOPT_FOLLOWLOCATION, true);
	    curl_setopt($ch, CURLOPT_URL, $url);
	    curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, FALSE);
     	curl_setopt($ch, CURLOPT_PROXY, "forward.xdaili.cn:80"); 
	    curl_setopt($ch, CURLOPT_TIMEOUT,120);
		curl_setopt($ch, CURLOPT_CONNECTTIMEOUT,6);
	    curl_setopt($ch, CURLOPT_RETURNTRANSFER, 1);
        $text = curl_exec($ch);
        curl_close($ch);
        var_dump($text);
	}
