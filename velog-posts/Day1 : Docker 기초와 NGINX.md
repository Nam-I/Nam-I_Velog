<h2 id="✊개념-잡기">✊개념 잡기</h2>
<blockquote>
<p><strong>Docker</strong>
<strong>도커(docker)</strong>는 컨테이너라는 기술을 사용해서 애플리케이션을 언제 어디서나, 같은 환경에서 배포하고 실행할 수 있게 해주는 도구입니다.</p>
</blockquote>
<blockquote>
<p><strong>Container</strong>
<strong>컨테이너</strong> 기술은 각 애플리케이션이 서로의 실행 환경에 영향을 받지 않고 독립적으로 실행할 수 있게 해주는 기술이고, <strong>도커</strong>는 이 컨테이너 기술을 편리하게 사용할 수 있게 해주는 도구입니다.</p>
</blockquote>
<blockquote>
<p><strong>Docker image</strong></p>
</blockquote>
<ul>
<li>Application을 포장 및 전송하기 위해 도커는 &quot;docker image&quot;를 사용합니다.
Docker image는 파일로 어플리케이션 실행에 필요한 독립적인 환경을 포함하며, 런타임 환경을 위한 일종의 템플릿입니다.</li>
<li>도커 이미지는 소스 코드, 라이브러리, 종속성, 도구 및 응용 프로그램을 실행하는데 필요한 기타 파일을 포함하는** 불변(변경 불가) 파일로**, 이미지는 읽기 전용이므로 스냅샷이라고도 하며, 특정 시점의 애플리케이션과 가상 환경을 나타냅니다.</li>
<li>이러한 일관성은 도커의 큰 특징 중 하나로 <strong>개발자가 안정적이고 균일한 조건에서 소프트웨어를 테스트하고 실험할 수 있도록 합니다.</strong></li>
</ul>
<blockquote>
<p><strong>Registry</strong>
만든 이미지를 보관하는 장소입니다.</p>
</blockquote>
<blockquote>
<p><strong>Docker Hub</strong>
도커에서 관리하는 저장소. 전세계 사람들이 만든 Docker 이미지를 공유하고 내려 받을 수 있는 공식 이미지 저장소입니다.</p>
</blockquote>
<blockquote>
<p><strong>Network</strong>
독립적인 컨테이너끼리 데이터를 주고 받을 수 있도록 해줍니다.</p>
</blockquote>
<blockquote>
<p><strong>volume</strong>
데이터를 다루는 컨테이너에 설정하여 개발자가 지정한 경로를 동기화 시켜주는 역할을 합니다.</p>
</blockquote>
<blockquote>
<p><strong>NGINX</strong>
클라이언트의 요청을 여러 서버로 분산시켜서 서버의 부하를 감소시키는 역할을 합니다.</p>
</blockquote>


<h2 id="🥊실습하기">🥊실습하기</h2>
<h3 id="🥊실습-1--이미지와-컨테이너명-포트-지정하여-nginx-실행해보기">🥊실습 1 : 이미지와 컨테이너명, 포트 지정하여 nginx 실행해보기</h3>
<p><code>docker run --name &lt;컨테이너이름&gt; -d -p &lt;호스트포트&gt;:&lt;컨테이너포트&gt; &lt;이미지이름&gt;</code></p>
<ul>
<li>도커 이미지와 컨테이너 생성 후 컨테이너를 실행하는 명령어 형식</li>
<li>위 명령어의 동작 순서<ul>
<li>지정한 이미지가 로컬에 있으면 사용, 없으면 Docker Hub에서 다운로드</li>
<li>지정한 이름의 컨테이너 생성</li>
<li>호스트포트, 컨테이너 포트 열기</li>
<li>컨테이너 실행</li>
</ul>
</li>
</ul>


<p><strong>내가 사용한 형식</strong>
<code>docker run --name server -d -p 8080:80 nginx</code></p>
<ul>
<li>컨테이너명: server</li>
<li>이미지명: nginx</li>
<li>호스트포트: 8080  &lt;= 로컬에서 접속하는 포트</li>
<li>컨테이너 포트: 80  &lt;= 컨테이너에 접근하는 포트</li>
</ul>


<p><strong>추가로 사용한 명령어</strong>
<code>docker ps</code> &emsp; =&gt; 실행중인 컨테이너 목록 보기
<code>docker ps -a</code> &emsp;  =&gt; 모든 컨테이너의 실행상태 보기(-a는 all을 뜻함)
<code>docker start &lt;컨테이너명&gt;</code> &emsp; =&gt; 해당 컨테이너 실행
<code>docker stop &lt;컨테이너명&gt;</code> &emsp; =&gt; 해당 컨테이너 중단
<code>docker exec -it &lt;컨테이너명&gt; /bin/bash</code> &emsp; =&gt; 컨테이너 내부에 들어가기</p>


<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/1eb4364a-5c5e-41cb-a33a-40bb1378faca/image.png" /></p>
<ul>
<li><code>docker run --name server -d -p 8080:80 nginx</code>
  : &quot;nginx&quot; 이미지로 &quot;server 컨테이너 생성 및 실행</li>
<li><code>docker ps</code>
  :실행 중인 컨테이너 목록 보기</li>
<li><code>docker start server</code>
  : &quot;server&quot; 컨테이너 실행</li>
<li><code>docker stop server</code>
  : &quot;server&quot; 컨테이너 중단</li>
</ul>


<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/16fc0660-7ec5-4619-975f-b0e36a0ece54/image.png" /></p>
<ul>
<li>localhost:8080 으로 들어가보면 nginx 가 잘 실행되는 것을 확인할 수 있다.</li>
</ul>


<hr />
<br />

<h3 id="🥊실습-2--html을-nginx-이미지로-열기">🥊실습 2 : html을 nginx 이미지로 열기</h3>
<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/c3752995-0282-42e9-af44-bcc534b87661/image.png" /></p>
<ul>
<li>원하는 경로 폴더에 index.html 파일 만들기</li>
</ul>


<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/d973cb84-512e-4fbc-99d9-d3f35e81c37f/image.png" /></p>
<ul>
<li><code>docker run --name server -d -p 8080:80 -v ${pwd}/index.html:/usr/share/nginx/html/index.html nginx</code>
=&gt; index.html 을 nginx 이미지로 열기 위한 명령어(컨테이너는 &quot;server&quot; 사용)</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/a52d5644-e21f-424c-9b77-01ab649c5755/image.png" /></p>
<ul>
<li><code>docker ps</code> 명령어를 실행해보면 컨테이너가 잘 실행 중인 것을 확인할 수 있다.</li>
</ul>
<p><img alt="" src="https://velog.velcdn.com/images/namiaow/post/3d63d0f7-bc62-4331-bc24-7837243082a5/image.png" /></p>
<ul>
<li>다시 localhost:8080 으로 들어가보면 index.html 이 nginx 이미지로 열린 것을 확인할 수 있다.</li>
</ul>


<hr />
 <br />

<h3 id="🥊실습-3--데이터베이스-컨테이너-생성하기">🥊실습 3 : 데이터베이스 컨테이너 생성하기</h3>
<p><code>docker run --name database -d -p 3307:3306 -e MYSQL_ROOT_PASSWORD=1234 -e MYSQL_DATABASE=backend mysql:8.0</code></p>
<ul>
<li>&quot;database&quot; 라는 이름의 컨테이너 만들기</li>
<li>컨테이너 시작 시 &quot;backend&quot; 라는 이름의 데이터베이스를 자동 생성</li>
<li>사용할 Docker 이미지 (MySQL 버전 8.0)</li>
</ul>
<br />

<p><strong>🗃️명령어 표로 정리하기</strong></p>
<table>
<thead>
<tr>
<th>옵션</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><strong><code>--name database</code></strong></td>
<td>컨테이너 이름을 <code>database</code>로 설정합니다.</td>
</tr>
<tr>
<td><strong><code>-d</code></strong></td>
<td>Detached 모드로, 백그라운드에서 컨테이너를 실행합니다.</td>
</tr>
<tr>
<td><strong><code>-p 3307:3306</code></strong></td>
<td>호스트의 포트 3307을 컨테이너의 MySQL 기본 포트 3306에 매핑합니다. <br />즉, 호스트에서는 <code>localhost:3307</code>로 접근할 수 있습니다.</td>
</tr>
<tr>
<td><strong><code>-e MYSQL_ROOT_PASSWORD=1234</code></strong></td>
<td>MySQL 루트 계정의 비밀번호를 <code>1234</code>로 설정합니다.</td>
</tr>
<tr>
<td><strong><code>-e MYSQL_DATABASE=backend</code></strong></td>
<td>컨테이너 시작 시 <code>backend</code>라는 이름의 데이터베이스를 자동으로 생성합니다.</td>
</tr>
<tr>
<td><strong><code>mysql:8.0</code></strong></td>
<td>사용할 Docker 이미지로, <code>MySQL 8.0</code> 버전을 명시합니다.</td>
</tr>
</tbody></table>
<br />

<ul>
<li><p>MySQL WorkBench 실행 후 데이터 입력</p>
</li>
<li><p><code>docker rm -f database</code>  ⇒ 데이터베이스 컨테이너 삭제</p>
</li>
<li><p>데이터베이스 컨테이너 삭제 후 다시 같은 내용으로 컨테이너를 다시 생성해도 데이터가 그대로 남아있는 것을 확인할 수 있습니다.</p>
</li>
</ul>
<br />

<hr />
<br />

<h3 id="🥊실습-4--nginxconf-파일-활용해-네트워크-설정하기">🥊실습 4 : nginx.conf 파일 활용해 네트워크 설정하기</h3>
<p><strong>✊개념 잡기</strong></p>
<blockquote>
<p><strong>nginx.conf 파일의 역할</strong></p>
</blockquote>
<ul>
<li>nginx.conf 파일은 Nginx 웹 서버의 핵심 설정 파일입니다. </li>
<li>이 파일은 Nginx가 어떻게 작동할지를 전반적으로 제어하는 역할을 합니다.</li>
<li>웹 서버 역할, 정적 파일 서빙, 리버스 프록시, 보안 설정(SSL) 등 모든 것을 제어합니다.</li>
</ul>
<table>
<thead>
<tr>
<th>구분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td>🔧 <strong>전역 설정</strong></td>
<td>프로세스 수(<code>worker_processes</code>), 로그 파일 위치, PID 파일 등 Nginx의 전반적인 동작 방식 지정</td>
</tr>
<tr>
<td>🌐 <strong>HTTP 서버 설정</strong></td>
<td>클라이언트 요청을 처리할 HTTP 서버의 기본 설정 정의 <br />예: <code>keepalive_timeout</code>, <code>gzip</code>, <code>client_max_body_size</code> 등</td>
</tr>
<tr>
<td>📂 <strong>서버 블록 설정</strong> (<code>server</code>)</td>
<td>도메인별 가상 호스트 설정 <br />예: <code>listen 80</code>, <code>server_name</code>, <code>location</code> 등</td>
</tr>
<tr>
<td>📁 <strong>위치(location) 설정</strong></td>
<td>요청 URL 경로에 따라 리소스를 어떻게 처리할지 결정 <br />예: 정적 파일 경로, 프록시 설정, 리디렉션 등</td>
</tr>
<tr>
<td>🔄 <strong>리버스 프록시 설정</strong></td>
<td>다른 서버(API, 백엔드 등)로 요청을 전달하고 응답을 받아 처리 가능</td>
</tr>
<tr>
<td>🔒 <strong>SSL 설정 (선택)</strong></td>
<td>HTTPS 연결 시 사용될 인증서와 키 설정 가능</td>
</tr>
</tbody></table>
<br />

<p><strong>nginx.conf 파일 설정</strong>
<img alt="" src="https://velog.velcdn.com/images/namiaow/post/b0fefd3b-ef9f-4fc6-ab3f-115be837f007/image.png" /></p>
<br />


<p><strong>사용한 명령어</strong></p>
<ul>
<li><code>docker build -t &lt;이미지 이름&gt;:&lt;태그&gt;&lt;Dockerfile&gt;경로</code> &emsp; =&gt; 도커 이미지를 만드는 명령어</li>
<li><code>docker images</code> &emsp; =&gt; 만들어진 이미지들 보기</li>
<li><code>docker run --name &lt;컨테이너 이름&gt; -d -p 8050:8080 &lt;이미지 이름&gt;</code> &emsp; =&gt; 설정한 이미지 이름과 컨테이너 이름으로 컨테이너 생성 및 실행</li>
<li><code>docker rm -f &lt;컨테이너 이름&gt;</code> &emsp; =&gt; 해당하는 컨테이너 지우기</li>
<li><code>docker network create &lt;네트워크 이름&gt;</code> &emsp; =&gt; 지정한 이름으로 네트워크 생성</li>
<li><code>docker run --name &lt;컨테이너 이름&gt; -d -p 80:80 -v ${pwd}/nginx/nginx.conf:/etc/nginx/nginx.conf --network &lt;생성한 네트워크 이름&gt; &lt;이미지 이름&gt;</code> &emsp; =&gt; 네트워크에 연결된 nginx 컨테이너(컨테이너 이름은 다를 수 있음)를 생성하고 실행하는 명령어</li>
</ul>
<br />

<p><strong>내가 사용한 방식</strong></p>
<ul>
<li><code>docker build -t backend .</code> &emsp; =&gt; 현재 디렉토리에 Dockerfile을 찾아 &quot;backend&quot; 라는 이름의 이미지 빌드</li>
</ul>
<p><strong>🗃️명령어 표로 정리하기</strong></p>
<table>
<thead>
<tr>
<th>부분</th>
<th>설명</th>
</tr>
</thead>
<tbody><tr>
<td><code>docker build</code></td>
<td>도커 이미지 생성(build) 명령어</td>
</tr>
<tr>
<td><code>-t backend</code></td>
<td>생성할 이미지의 태그(tag)를 <code>backend</code>로 지정 (<code>-t</code>는 <code>--tag</code>의 약어)</td>
</tr>
<tr>
<td><code>.</code></td>
<td>현재 디렉토리에서 <code>Dockerfile</code>을 찾아 이미지를 빌드하라는 의미</td>
</tr>
</tbody></table>
<ul>
<li><p><code>docker run --name backend -d -p 8050:8080 backend</code>  &emsp; ⇒ &quot;backend&quot; 라는 이름의 이미지를 사용한 &quot;backend&quot;라는 이름의 컨테이너 생성 및 실행</p>
</li>
<li><p><code>docker network create my-network</code> &emsp; ⇒ &quot;my-network&quot; 라는 이름의 네트워크 생성</p>
</li>
<li><p><code>docker run --name nginx -d -p 80:80 -v ${pwd}/nginx/nginx.conf:/etc/nginx/nginx.conf --network my-network nginx</code> &emsp; =&gt; nginx.conf 설정 파일에 따라 네트워크를 설정하고 생성한 Docker 네트워크 &quot;my-network&quot; 에 연결. 이미지 이름 &quot;nginx&quot;, 컨테이너 이름 &quot;nginx&quot;</p>
</li>
</ul>
<br />

<p><strong>⚠️주의점</strong></p>
<ul>
<li><span style="background-color: #FFF6B9;"><strong>nginx.conf 파일에 설정한 경로와 생성한 컨테이너의 포트 설정 정보가 동일한지 꼭 확인!</strong></span></li>
</ul>
<br />

<ul>
<li><p>모든 설정이 올바르게 잘 되었다면 도커 컨테이너가 잘 생성된 것을 확인할 수 있다.
<img alt="" src="https://velog.velcdn.com/images/namiaow/post/968921a5-4a5b-4958-ab25-6e40af72e019/image.png" /></p>
</li>
<li><p>ninx.conf 의 nginx 네트워크 호스트포트, 컨테이너 포트 80:80 =&gt; 도커에서도 올바르게 잘 생성됨</p>
</li>
<li><p>nginx.conf 의 backend 컨테이너의 컨테이너 포트 8080 =&gt; 도커에서도 올바르게 잘 생성됨. (호스트 포트 8050, 컨테이너 포트 8080)</p>
</li>
</ul>
<br />

<hr />
<br />

<h3 id="🥊실습-5--서버-분산해서-실행하기">🥊실습 5 : 서버 분산해서 실행하기</h3>
<ul>
<li>nginx.conf 파일 수정<pre><code>worker_processes 1;
</code></pre></li>
</ul>
<p>events {
    worker_connections 1024;
}</p>
<p>http {
    upstream spring_backend {
        server backend1:8080;
        server backend2:8080;
        server backend3:8080;
    }</p>
<pre><code>server {
    listen 80;

    location / {
        proxy_pass http://spring_backend/api;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
}</code></pre><p>}</p>
<pre><code>
&lt;br&gt;

- docker-compose.yml 파일 수정</code></pre><p>services:</p>
<p>  backend1:  # 서비스 이름은 컨테이너간 통신하기 위한 이름
    image: backend
    container_name: backend1
    environment:
      PROJECT_NAME: 백앤드 서버1
  backend2:  # 서비스 이름은 컨테이너간 통신하기 위한 이름
    image: backend
    container_name: backend2
    environment:
      PROJECT_NAME: 백앤드 서버2
  backend3:  # 서비스 이름은 컨테이너간 통신하기 위한 이름
    image: backend
    container_name: backend3
    environment:
      PROJECT_NAME: 백앤드 서버3</p>
<p>  nginx:
    image: nginx:1.25
    container_name: nginx
    ports:
      - &quot;80:80&quot;
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
    depends_on:
      - backend1
      - backend2
      - backend3</p>
<p>```</p>
<br />

<ul>
<li><p><code>docker compose up -d</code> &emsp; =&gt; 도커 컴포즈 명령어로 컨테이너 생성 및 실행. 이미지를 하나하나 생성해야 하는 번거로움을 없애준다.</p>
</li>
<li><p>설정을 완료한 후 localhost 경로로 접속해 새로고침 해보면 새로고침 시마다 다른 서버로 동작하는 것을 확인할 수 있다.</p>
</li>
</ul>
<br />

<p><strong>인텔리제이에서 jar 파일 만들기</strong>
<img alt="" src="https://velog.velcdn.com/images/namiaow/post/0afeaf07-be70-4e1c-a1b5-7c4fb5b2bf0a/image.png" /></p>
<ul>
<li>우측 Gradle 버튼 섹션 클릭 -&gt; backendProject\Task\build 에서 &quot;bootJar&quot; 더블 클릭</li>
</ul>
<br />

<hr />
<br />

<h2 id="❤-느낀점">❤ 느낀점</h2>
<span style="background-color: #FFD9FA;">
  반복해서 이미지와 컨테이너를 생성해보고 시행착오를 겪어보니 도커의 이미지, 컨테이너의 상호작용과 동작 방식을 명확하게 이해할 수 있었습니다.
</span>