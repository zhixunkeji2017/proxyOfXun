    <?php
      //生成token
      function get_token($spider_id, $secret, $params) {
        $spider_id = ""; //登录后在个人中心获取
        $secret = "";   //登录后在个人中心获取

        //参数排序
        ksort($params);
        //参数拼接
        $param_str = "";
        foreach($params as $key=>$value) {
          if(gettype($value) != 'array'){
            $param_str .= $key;
            $param_str .= $value;
          }else{
            $param_str .= ($key."{\"");
            foreach($value as $key=>$value) {
              $param_str .= $key."\":\"";
              $param_str .= $value;
            }
            $param_str .= "\"}";
            var_dump($param_str);
          }
        }
        //生成sha1签名
        $param_str = sha1($param_str, false);
        $sign = strtoupper($param_str);

        $timestamp = get_time();
        //MD5生成token
        $token = md5($timestamp.$secret.$sign);
        return array("token"=>$token, "timestamp"=>$timestamp, "spiderId"=>$spider_id, "Content-Type"=>"application/json");
      }

      // 获取时间戳
      function get_time(){
        $api_url="http://api.xdaili.cn/xdaili-api/privateProxy/getTime";

        $ch = curl_init($api_url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "GET");
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
        $result = curl_exec($ch);
        curl_close($ch);

        $rsArray = explode("\r\n\r\n", $result);
        return json_decode($rsArray[1], true)["RESULT"];
      }

      //独享动态
      //批量申请拨号服务器接口
      function batch_apply() {
        $spider_id = ""; //登录后在个人中心获取
        $secret = "";   //登录后在个人中心获取

        $api_url="http://api.xdaili.cn/xdaili-api/spider/applyChannels";

        $params = array("count" => 1);
        $data_string = json_encode($params);
        $headers = get_token($spider_id, $secret, $params);

        $ch = curl_init();
        curl_setopt($ch, CURLOPT_URL, $api_url);
        curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
        curl_setopt($ch, CURLOPT_POSTFIELDS,$data_string);
        curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($ch, CURLOPT_HEADER, true);
        curl_setopt($ch, CURLOPT_HTTPHEADER,array(
          "token:".$headers["token"],
          "spiderId:".$headers["spiderId"],
          "timestamp:".$headers["timestamp"],
          "Content-Type:application/json"
        ));
        curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
        $result = curl_exec($ch);
        curl_close($ch);

        echo $result;
      }

      //拨号接口
    function get_dynamic_ip() {
      //proxyId和orderno分别替换成相应的值
      $api_url = "http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP/orderno/proxyId";
      $headers = get_token($spiderId, $secret, array());

      $ch = curl_init($api_url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HEADER, true);
      curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
      $result = curl_exec($ch);
      curl_close($ch);

      echo $result;
    }

    //注销通道拨号服务器
    function batch_logout() {
      $spider_id = ""; //登录后在个人中心获取
      $secret = "";   //登录后在个人中心获取

      $api_url = "http://api.xdaili.cn/xdaili-api/spider/logOut";
      //proxyId和orderno分别替换成相应的值
      $data = array("map"=>array("proxyId"=>"orderno"));
      $headers = get_token($spider_id, $secret, $data);
      $data_string = json_encode($data);

      $ch = curl_init($api_url);
      curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "POST");
      curl_setopt($ch, CURLOPT_POSTFIELDS,$data_string);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HEADER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        "token:".$headers["token"],
        "spiderId:".$headers["spiderId"],
        "timestamp:".$headers["timestamp"],
        "Content-Type:application/json"
      ));
      curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
      $result = curl_exec($ch);
      curl_close($ch);

      echo $result;
    }

    //注销全部接口
    function logout_all() {
      $spider_id = ""; //登录后在个人中心获取
      $secret = "";   //登录后在个人中心获取

      $api_url = "http://api.xdaili.cn/xdaili-api/spider/logOutAll";
      $headers = get_token($spiderId, $secret, array());

      $ch = curl_init($api_url);
      curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
      curl_setopt($ch, CURLOPT_HEADER, true);
      curl_setopt($ch, CURLOPT_HTTPHEADER, array(
        "token:".$headers["token"],
        "spiderId:".$headers["spiderId"],
        "timestamp:".$headers["timestamp"],
        "Content-Type:application/json"
      ));
      curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
      $result = curl_exec($ch);
      curl_close($ch);

      echo $result;
    }
    ?>
    
