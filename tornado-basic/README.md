<h1>tornado framework study note </h1>

<h2>1.siege 文档 <a href="https://www.joedog.org/siege-manual/">https://www.joedog.org/siege-manual/</a></h2>

<h2>2.siege 安装</h2>
<h3>wget http://download.joedog.org/siege/siege-3.1.4.tar.gz</h3>
<h3>./configure && make && make install </h3>

<h2>3.siege 压测</h2>
<h3>50个并发请求，持续10s </h3>
<h3>siege http://localhost:8000/ -c50 -t10s </h3>

<h2>4.部署</h2>
<h3><a href="http://www.kancloud.cn/kancloud/introduction_to_tornado/61352">nginx + tornado 多实例</a></h3>

<h2>5.ref resources </h2>
<h3>http://www.kancloud.cn/kancloud/introduction_to_tornado/61347 </h3>
<h3>http://www.tornadoweb.org/en/stable/</h3>
