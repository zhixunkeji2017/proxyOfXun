//申请通道
   let timestamp = parseInt(new Date().getTime()/1000);

    //2 对除了head信息外的参数名进行排序拼接
    let params = {count:1}
    function keys(params){
      let arr = [];
      for(let i in params){
        arr.push(i + params[i])
      }
      return arr.sort().join('')
    }

    // 3 计算参数的sign(使用SHA1生成签名）
    let shasum = crypto.createHash('sha1');
    shasum.update(keys(params));
    let sign = shasum.digest('hex');
    sign = sign.toUpperCase();

    // 4 混合计算MD5(timestamp时间戳 + secret密钥 + sign签名）
    let secret = '9049fd015e2c41e3a5081f6b48b56c0e';//讯代理个人信息获取secret

    let md5 = crypto.createHash('md5');
    md5.update(timestamp + secret + sign);
    let token = md5.digest('hex');

    // 5 header添加时间戳和token 请求接口
    let options = {
        url: 'http://api.xdaili.cn/xdaili-api/spider/applyChannels',
        json: true,
        headers: {
            'Accept':'*/*',
            'timestamp': timestamp,
            'token':token,
            'spiderId':'2e086cc149f24dccb471f1d122db7deb'//讯代理个人信息获取唯一标志码
        },
        body:{
          "count":1
        }
    };
    function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
            // let info = JSON.parse(body);
            console.log(body)
        }
    }
    request(options, callback);
    
    //拨号
    
        let options = {
        url: 'http://api.xdaili.cn/xdaili-api/privateProxy/getDynamicIP/DD201612263013CUpfvC/565910f2b79811e6802371d9ec16a600'
    };
    function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
        }
    }
    request(options, callback);
    
    
    //注销
    
        let options = {
        url: 'http://api.xdaili.cn/xdaili-api/spider/logOut',
        json: true,
        headers: {
            'Accept':'*/*',
            'timestamp': timestamp,
            'token':token,
            'spiderId':'2e086cc149f24dccb471f1d122db7deb'//讯代理个人信息获取唯一标志码
        },
        body:{
          "map" : {
               "565910f2b79811e6802371d9ec16a600":"DD201612263013CUpfvC"
          }
        }
    };
    function callback(error, response, body) {
        if (!error && response.statusCode == 200) {
            console.log(body)
        }
    }
    request(options, callback);
    
    //退出全部
    
        let options = {
        url: 'http://api.xdaili.cn/xdaili-api/spider/logOutAll',
        json: true,
        headers: {
            'Accept':'*/*',
            'timestamp': timestamp,
            'token':token,
            'spiderId':'2e086cc149f24dccb471f1d122db7deb'//讯代理个人信息获取唯一标志码
        }
    };
    function callback(error, response, body) {
        if (!error &&  response.statusCode == 200) {
            console.log(body)
        }
    }
    request(options, callback);
    
 
 
