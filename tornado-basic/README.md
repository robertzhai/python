<h1>tornado framework study note </h1>

<h2>1.siege 文档 <a href="https://www.joedog.org/siege-manual/">https://www.joedog.org/siege-manual/</a></h2>
<h2>2.siege 安装</h2>
<h3>    wget http://download.joedog.org/siege/siege-3.1.4.tar.gz</h3>
<h3>    ./configure && make && make install </h3>
<h2>siege 压测</h2>
<h3>    50个并发请求，持续10s </h3>
<h3>    siege http://localhost:8000/ -c50 -t10s </h3>
