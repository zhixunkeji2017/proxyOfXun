
const crypto = require('crypto');
const request = require('request');

let timestamp = parseInt(new Date().getTime()/1000);
let url = 'http://www.baidu.com/';
let orderno = 'ZF20179xxxxxxxxx';
let secret = 'cb65091847ad42fxxxxxxx';

let plantext = 'orderno='+orderno+',secret='+secret+',timestamp='+timestamp;
let md5 = crypto.createHash('md5');
md5.update(plantext);
let sign = md5.digest('hex');
sign = sign.toUpperCase();

let options = {
    url:url,
    proxy: "http://forward.xdaili.cn:80",
    headers:{
      'Proxy-Authorization':'sign='+sign+'&orderno='+orderno+"&timestamp="+timestamp
    }
};
function callback(error, response, body) {
  console.log(response)
  if (!error && response.statusCode == 200) {
      console.log(body)
      return false
  }
  console.log(error)
}
request(options, callback);
