/**
 * 同时支持 http 以及 https
 * yarn add xdaili-fetch node-fetch
 */
const Xfetch = require('xdaili-fetch');
const fetch = Xfetch(require('node-fetch'), {
    orderno: '??',
    secret: '??'
});

fetch('https://www.baidu.com')
  .then(d=>d.text())
  .then(console.log)
  .catch(console.error)
