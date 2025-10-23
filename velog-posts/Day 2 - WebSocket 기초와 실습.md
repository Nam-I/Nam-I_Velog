<h2 id="✊개념-잡기">✊개념 잡기</h2>
<br />

<p><strong>HTTP Polling VS HTTP Long Polling</strong></p>
<table>
<thead>
<tr>
<th>항목</th>
<th>HTTP Polling</th>
<th>HTTP Long Polling</th>
</tr>
</thead>
<tbody><tr>
<td>🧭 동작 방식</td>
<td>클라이언트가 일정 주기로 계속 요청</td>
<td>클라이언트가 요청을 보내고, <strong>데이터가 생길 때까지 대기</strong></td>
</tr>
<tr>
<td>🔁 요청 빈도</td>
<td>짧은 주기로 자주 보냄</td>
<td>필요할 때만 재요청</td>
</tr>
<tr>
<td>🧠 서버 부하</td>
<td><strong>많은 요청</strong> 처리 필요 → 부하 큼</td>
<td>요청 수가 적어 상대적으로 부하가 적음</td>
</tr>
<tr>
<td>📥 응답 타이밍</td>
<td>즉시 응답 (데이터가 없어도)</td>
<td>데이터 생기면 응답</td>
</tr>
<tr>
<td>📦 실시간성</td>
<td>낮음 (최신 데이터를 놓칠 수 있음)</td>
<td>높음 (거의 실시간에 가깝게 데이터 수신)</td>
</tr>
<tr>
<td>🔌 연결 지속 시간</td>
<td>짧음 (매번 연결을 다시 맺음)</td>
<td>길음 (요청이 대기 상태로 유지됨)</td>
</tr>
<tr>
<td>🚀 사용 예시</td>
<td>뉴스 피드 갱신, 주기적인 상태 체크</td>
<td>채팅, 알림 시스템 등 실시간성이 중요한 경우</td>
</tr>
</tbody></table>
<br />

<p><strong>📌요약</strong></p>
<ul>
<li><p>HTTP Polling은 반복적으로 &quot;새로 생긴 게 있니?&quot;라고 묻는 방식이고,</p>
</li>
<li><p>HTTP Long Polling은 &quot;생기면 알려줘&quot;라고 하고 기다리는 방식입니다.</p>
</li>
</ul>
<blockquote>
<p>실시간성을 높이고 네트워크 자원을 줄이려면 Long Polling이 더 유리하지만,
궁극적으로는 WebSocket이나 SSE(Server-Sent Events) 같은 기술로 가는 게 효율적입니다.</p>
</blockquote>
<br />

<hr />
<br />

<p><strong>WebSocket 이란?</strong></p>
<ul>
<li><p><strong>WebSocket</strong> 은 클라이언트와 서버 간의 지속적인 연결을 유지하고 <strong>양방향 통신</strong>이 가능한 프로토콜입니다.</p>
</li>
<li><p>요청-응답 모델을 사용하는 기존 <strong>HTTP</strong>와 달리 <strong>WebSocket</strong>은 <span style="background-color: #FFF6B9;">새로운 연결을 반복적으로 설정하지 않고도 지속적으로 양방향 데이터 교환을 가능하게 합니다.</span> (채팅 어플리케이션, 온라인 게임, 주식 시세 등)</p>
<p align="ceter"><img height="60%" src="https://velog.velcdn.com/images/namiaow/post/2584d4b9-0b67-486c-b32a-7fb99c0e76a5/image.png" width="60%" /><p>
</li>
<li><p><span style="background-color: #FFF6B9;"><strong>WebSocket 도 연결을 하기 위해서 최초에 한 번은 HTTP 요청을 보냅니다.</strong></span></p>
</li>
<li><p>WebSocket 사용 플랫폼 예: 배달의 민족 라이더 위치 서비스</p>
<p align="center"><img src="https://velog.velcdn.com/images/namiaow/post/4e5be56d-9d61-4964-86be-9d1bbd8310f8/image.png" width="50%" /></p>

</li>
</ul>
<br />

<hr />
<br />

<p><strong>Spring 에서 WebSocket 을 사용하는 대표적인 두가지</strong></p>
<ul>
<li>Spring WebSocket</li>
<li>Spring WebSocket + STOMP</li>
</ul>
<br />

<h3 id="1-spring-websocket">1. Spring WebSocket</h3>
<ul>
<li><p>특징 : 연결만 제공하고 핸들러를 직접 구현해야 한다.</p>
</li>
<li><p><strong>session</strong> : 연결된 상태를 관리하는 객체</p>
<pre><code>public class ChatWebSocketHandler extends TextWebSocketHandler {

  //세션을 관리하는 객체
  // Collections.synchronizedSet &lt;- 여러 스레드가 동시에 이 객체에 접근할 때 동시설 문제를 안전하게 만들어주는 역할
 // 동시성 문제를 해결 - 서버에 여러 클라이언트 접속 시에 발생할 수 있는 데이터 손실 고려
  private final Set&lt;WebSocketSession&gt; sessions = Collections.synchronizedSet(new HashSet&lt;&gt;());

  // json 문자열 -&gt; 자바 객체로 변환
  private final ObjectMapper objectMapper = new ObjectMapper();

  //방과 방 안에 있는 세션을 관리하는 객체
  private  final Map&lt;String, Set&lt;WebSocketSession&gt;&gt; rooms = new ConcurrentHashMap&lt;&gt;(); //&lt;-동시성 문제 해결을 위해 사용

</code></pre></li>
</ul>
<pre><code>// 클라이언트가 보낸 메세지를 서버가 받았을 때 호출
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage message)
        throws Exception {
    super.handleTextMessage(session, message);

    // json 문자열 -&gt; 자바 객체
    ChatMessage chatMessage = objectMapper.readValue(message.getPayload(), ChatMessage.class);

    String roomID = chatMessage.getRoomId(); //클라이언트에게 받은 메세지에서 roomID를 추출

    if(!rooms.containsKey(roomID)){ //방을 관리하는 객체에 현재 세션이 들어가는 방이 있는지 확인
        rooms.put(roomID, ConcurrentHashMap.newKeySet());  //없으면 새로은 방을 생성
    }
    rooms.get(roomID).add(session); //해당 방에 세션 추가


    for(WebSocketSession s : rooms.get(roomID)) {
    //for (WebSocketSession s : sessions) {
        if (s.isOpen()) {
            s.sendMessage(new TextMessage(objectMapper.writeValueAsString(chatMessage)));

            System.out.println(&quot;전송된 메세지 = &quot; +chatMessage.getMessage());
        }
    }
}


// 클라이언트가 웹 소켓 서버에 접속했을 때 호출
@Override
public void afterConnectionEstablished(WebSocketSession session) throws Exception {
    super.afterConnectionEstablished(session);
    sessions.add(session);      // 연결된 클라이언트 저장
    System.out.println(&quot;접속된 클라이언트 세션 ID = &quot; + session.getId());
}

// 클라이언트가 연결이 끊어졌을 때 호출
@Override
public void afterConnectionClosed(WebSocketSession session, CloseStatus status)
        throws Exception {
    super.afterConnectionClosed(session, status);

    sessions.remove(session);

    //연결이 해제되면 소속되어 있는 방에서 제거
    for(Set&lt;WebSocketSession&gt; room : rooms.values()) {
        room.remove(session);
    }
}</code></pre><p>}</p>
<pre><code>
&lt;br&gt;

**순수 WebSocket 메세지**

- 그냥 문자열(텍스트/바이너리)만 주고 받음
예시:
&lt;img src=&quot;https://velog.velcdn.com/images/namiaow/post/bd11edb3-2562-40b0-bf5e-dbcd2cde7fc1/image.png&quot; width=80%&gt;

- 서버/클라이언트가 **&quot;어떤 의미인지, 누구한테 보내는지&quot;** &lt;u&gt;따로 해석해야 한다.&lt;/u&gt;(정해진 규약이 없음)


&lt;br&gt;

### 2. Spring WebSocket + STOMP
- STOMP (**S**imple **T**ext **O**riented **M**essaging **P**rotocol)
: 텍스트 기반의 메세지 전송 프로토콜
- 특징 : 채팅방(채널) 구분, 구독/발행, 메세지 라우팅을 STOMP 에서 자동 처리
- **WebSocket 위에서 동작하는 메세징 프로토콜**
- **메세지를 어떻게 주고 받을지의 규칙이 정해져 있음**</code></pre><p>@Controller
public class ChatController {
    @MessageMapping(&quot;/chat.sendMessage&quot;) 
    @SendTo(&quot;/topic/public&quot;)
    public ChatMessage sendMessage(ChatMessage message) {
        return message;
    }
}</p>
<pre><code>
&lt;br&gt;

### STOMP 프로토콜이 해주는 일
- **메세지 목적지(/topic/chat/room1, /queue/alert 등)를 헤더에 명시**
➡️ 어디로 라우팅 해야할지 서버가 쉽게 파악
- **SUBSCRIBE, UNSUBSCRIBE, SEND 등 명령어(Command)로 구분**
➡️ 클라이언트가 &quot;구독만&quot;, &quot;메세지만 보내기&quot;, &quot;해제&quot; 등 역할 분리
- **헤더/바디 분리**
➡️ 인증, 타입, 우선순위 등 부가 정보(헤더) 추가 가능
- **브로커가 각 채널 구독자에게만 자동으로 메세지 분배**

&lt;br&gt;

### STOMP 메세지 구조(예시)
- STOMP 는 명확한 **&quot;프레임&quot;** 구조를 가짐
-&gt; 메세지마다 &quot;명령(command)&quot;, &quot;헤더(header)&quot;, &quot;본문(body)&quot; 로 구성

&lt;br&gt;

**STOMP 메세지의 기본 형식**
&lt;img src=&quot;https://velog.velcdn.com/images/namiaow/post/0461bff4-8aff-4906-9a79-5befea68b510/image.png&quot; width=40%&gt;

- **COMMAND** : 메세지의 종류(SEND, SUBSCRIBE, CONNECT 등)
- **header** : 키-값 쌍(메세지의 목적지, 아이디 등등)
- **body** : 실제 메세지 내용
- **^@** : 메세지 끝(null 바이트, 숨겨진 제어문자)

&lt;br&gt;

**예시 : 클라이언트가 메세지를 서버에 전송(SEND)**
&lt;img src=&quot;https://velog.velcdn.com/images/namiaow/post/c941525e-119d-4afe-836a-ab976b1dc1f6/image.png&quot; width=40%&gt;

- **destination** : 메세지를 보낼 목적지(채팅방 등)
- **body** : 실제 전달할 데이터

&lt;br&gt;

**예시 : 클라이언트가 구독 요청(SUBSCRIBE)**
&lt;img src=&quot;https://velog.velcdn.com/images/namiaow/post/122b33d1-3687-43c0-9eca-402d5a296939/image.png&quot;  width=40%&gt;

- **id** : 구독 고유 값
- **destination** : 구독할 방(채널)

&lt;br&gt;

**예시 : 서버가 메세지 전달(MESSAGE)**
&lt;img src=&quot;https://velog.velcdn.com/images/namiaow/post/229039e5-5676-46ff-acba-7d55c79cffbc/image.png&quot; width=40%&gt;

- **subscription** : 어느 구독에 해당하는지
- **message-id** : 메세지 고유 ID
- **destination** : 어디에서 온 메세지인지
- **body** : 메세지 본문

&lt;br&gt;

---

&lt;br&gt;

## STOMP 를 많이 쓰는 이유
**1. 생산성과 유지 보수성**
- 채팅방, 알림, 구독/취소, 브로드캐스트 등의 기능을 다 내장하고 있음

**2. 코드가 간결하고 실수 가능성이 적음**
- 세션 관리, 채팅방 관리, 사용자 매핑, 목적지 라우팅 등을 다 코드로 직접 구현하면 버그도 많이 생기고, 개발자 마다 개발 방식이 달라 테스트/유지보수/협업 시 문제가 생길 가능성이 높음

**3. 확장성/변경 용이**
- 1:1 채팅방, 1:N 그룹방, 토픽별 알림 등을 STOMP 는 **경로만 바꾸면 적용** 가능
- 순수 WebSocket 은 내부 코드 구조도 전부 변경 필요

&lt;br&gt;

## 하지만 순수 WebSocket 을 써야 하는 상황은?
**1. 초고성능/초경량 통신이 필요할 때**
- 게임 서버, 초저지연 실시간 서비스
- 1ms 단위의 레이턴시가 중요한 상황
- 최대한 &quot;가공&quot; 을 없애고 패킷 크기를 최소화 하고 싶을 때
(STOMP 는 텍스트 기반 프레임, 헤더 등 오버헤드가 조금이라도 존재한다.)

**2. 메세지 구조를 직접 커스텀 해야 할 때**
- 사내 전용 메세지 포맷, 엔터프라이즈 표준, 바이너리 전용 등

**3. 아주 단순한 서비스**
- 채널/구독/방 기능이 필요 없는 경우
- 간단한 테스트용 데모 서버 등

&lt;br&gt;

**🗃️순수 WebSocket** VS **STOMP over WebSocket 비교하기 1**

| 항목             | 순수 WebSocket                      | STOMP over WebSocket                                        |
| -------------- | --------------------------------- | ----------------------------------------------------------- |
| 🧭 프로토콜 구조     | WebSocket만 사용                     | WebSocket 위에 STOMP 프로토콜 추가                                  |
| 🧩 메시지 포맷      | 바이너리 또는 텍스트 (자유 형식, JSON 등 직접 정의) | STOMP 형식 (프레임 기반: `SEND`, `SUBSCRIBE`, 등 명확함)               |
| ⚙️ 구현 난이도      | 낮음 (단순한 구조), 그러나 직접 구현 많음         | 높음 (초기 셋업 필요), 하지만 기능은 풍부                                   |
| 📦 내장 기능       | 없음 (구독, 대상, 헤더 등 직접 구현해야 함)       | 지원 (구독/발행, 헤더, ACK 등 표준화된 메시지 구조 지원)                        |
| 📬 메시지 라우팅     | 서버에서 직접 구현 필요                     | STOMP의 `destination` 기반으로 라우팅 가능                            |
| 💥 확장성/유지보수    | 구조가 단순하지만 기능 추가 시 복잡도 증가          | 미리 정의된 메시지 구조로 유지보수 쉬움                                      |
| 🧪 디버깅/가시성     | 메시지 구조 파악 어려움                     | 텍스트 기반 프레임 → 디버깅 쉬움                                         |
| 📘 표준 명세       | WebSocket (RFC 6455)              | WebSocket + STOMP (Simple Text Oriented Messaging Protocol) |
| 🧰 클라이언트 라이브러리 | 브라우저 WebSocket API                | `@stomp/stompjs`, `SockJS`, `spring-websocket` 등 사용         |
| 🔒 보안/인증       | 직접 처리해야 함                         | 메시지 헤더 등으로 인증 정보 쉽게 전달 가능                                   |
| 🌐 주요 사용 예시    | 게임, 채팅, 실시간 알림 (단순한 실시간 통신)       | 채팅, 알림, 주식 시세, 협업 앱 등 복잡한 실시간 기능                            |

&lt;br&gt;

**🗃️순수 WebSocket** VS **STOMP over WebSocket 비교하기 2**

| 항목            | 순수 WebSocket              | STOMP over WebSocket                      |
| ------------- | ------------------------- | ----------------------------------------- |
| **헤더**     | 거의 없음                     | 많음 (command, destination, content-type 등) |
| **형식**     | 이진/텍스트 가능                 | 텍스트 전용                                    |
| **오버헤드**   | 최소 (2\~14 bytes/frame)    | 큼 (헤더 수에 따라 50\~200 bytes 이상)             |
| **총 크기 예** | 약 115 bytes (100자 메시지 기준) | 300 bytes 이상                              |
| **실시간성**   | 매우 빠름                     | 약간의 딜레이 존재                                |
| **메시지 크기** | 작음 → 효율적                  | 큼 → 오버헤드 존재                               |
| **개발 난이도** | 낮음 (직접 구현 필요)             | 높지만 Spring에서는 자동 처리                       |
| **기능 지원**  | 직접 구현 (pub/sub, ACK 등)    | 내장 기능 많음 (구독, 구분, 에러 처리 등)                |

&lt;br&gt;

**🗃️순수 WebSocket VS STOMP over WebSocket 비교하기 3
**

| 구분           | 순수 WebSocket                                      | STOMP over WebSocket                            |
| ------------ | ------------------------------------------------- | ----------------------------------------------- |
| ✅ **성능**     | ✔ 매우 가볍고 빠름 &lt;br&gt;✔ 메시지 크기 작음 &lt;br&gt;✔ 오버헤드 거의 없음      | ❌ 상대적으로 무거움 &lt;br&gt;❌ 메시지 크기 큼 &lt;br&gt;❌ 헤더 많음 → 오버헤드 큼 |
| ✅ **기능**     | ❌ 기능 거의 없음 → 직접 pub/sub, ack, reconnect 등을 구현해야 함 | ✔ 구독, 라우팅, 에러 처리, 메시지 구분 등 내장 기능 풍부             |
| ✅ **개발 편의성** | ❌ 어렵고 수동 구현 많음                                    | ✔ Spring 등에서는 자동 지원으로 개발 쉬움                     |

&lt;br&gt;

---

&lt;br&gt;

## 📌요약

- **순수 WebSocket** :  **경량**이지만 기능을 **직접 만들어야 한다.**

- **STOMP over WebSocket** : **오버헤드가 있지**만 **기능이 풍부**하고 **Spring과 잘 통합**됩니다.

- 단순한 통신만 필요하고, 모든 처리를 직접 컨트롤하고 싶다. =&gt; **순수 WebSocket**
- &lt;u&gt;성능이 중요한 경우&lt;/u&gt;(예: 실시간 게임, 고빈도 메시징) =&gt; **순수 WebSocket**
: 빠르고 오버헤드 적음. 하지만 개발은 조금 힘들고 복잡함.
- 메시징 시스템처럼 구독/발행 구조, 메시지 형식화가 필요하다 =&gt; **STOMP over WebSocket**
- &lt;u&gt;기능과 개발 생산성이 중요한 경우&lt;/u&gt;(예: 실시간 채팅, 알림 시스템) =&gt; **STOMP over WebSocket**
: 기능이 이미 다 구현돼 있고, Spring 등에서 쉽게 사용 가능

- &lt;span style=&quot;background-color:#FFF6B9&quot;&gt;**상황과 필요에 따라 성능 ↔ 기능 사이에서 선택하면 됩니다!**&lt;/span&gt;

&lt;br&gt;

---

&lt;br&gt;

## ❤느낀점
&lt;span style=&quot;background-color:#FFD9FA&quot;&gt;
순수 WebSocket과 STOMP over WebSocket의 차이를 이해하고, Spring 을 활용해 두 가지 방식 모두를 사용한 WebSocket 통신을 구현해 볼 수 있었습니다. 지난 시간에 배운 Docker를 사용해 도커 컨테이너 서버로 접속해서 다수의 인원과 실시간으로 채팅을 할  수 있는 프로그램을 직접 개발하고 사용해 보는 과정이 즐거웠습니다.☺️
&lt;/span&gt;






</code></pre>