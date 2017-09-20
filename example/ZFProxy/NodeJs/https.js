
const crypto = require('crypto');
var url = require('url');
var https = require('https');
var HttpsProxyAgent = require('https-proxy-agent'); //第三方包,请安装

let timestamp = parseInt(new Date().getTime()/1000);
let orderno = 'ZF201797xxxxxxx';
let secret = 'cb65091847ad4xxxxxxxxxxxx';

let plantext = 'orderno='+orderno+',secret='+secret+',timestamp='+timestamp;
let md5 = crypto.createHash('md5');
md5.update(plantext);
let sign = md5.digest('hex');
sign = sign.toUpperCase();

// HTTP/HTTPS proxy to connect to
var proxy = process.env.http_proxy || 'http://forward.xdaili.cn:80';
console.log('using proxy server %j', proxy);

// HTTPS endpoint for the proxy to connect to
var endpoint = process.argv[2] || 'https://www.baidu.com';
console.log('attempting to GET %j', endpoint);
var options = url.parse(endpoint);
options.headers = {
  'Proxy-Authorization':'sign='+sign+'&orderno='+orderno+"&timestamp="+timestamp
}
options.rejectUnauthorized = false

// create an instance of the `HttpsProxyAgent` class with the proxy server information
var agent = new HttpsProxyAgent(proxy);
options.agent = agent;

https.get(options, function (res) {
  console.log('"response" event!', res.headers);
  res.pipe(process.stdout);
});
