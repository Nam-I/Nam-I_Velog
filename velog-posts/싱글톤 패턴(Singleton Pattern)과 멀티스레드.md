<h1 id="✊-개념-잡기-싱글톤-패턴이란">✊ 개념 잡기: 싱글톤 패턴이란?</h1>
<blockquote>
<p><strong>싱글톤 패턴(Singleton Pattern)</strong><br />특정 클래스의 인스턴스를 <strong>오직 하나만 생성</strong>하도록 보장하고,<br />프로그램 어디서든 <strong>같은 인스턴스에 접근할 수 있게 하는 디자인 패턴</strong>입니다.</p>
</blockquote>
<h3 id="🔑-쉽게-이해해보기">🔑 쉽게 이해해보기</h3>
<p>교실 문을 여는 <strong>마스터키</strong>가 있다고 상상해봅시다.<br />이 <strong>열쇠는 단 하나만</strong> 존재해야 해요.</p>
<p>왜냐하면...</p>
<ul>
<li>만약 똑같은 열쇠가 여러 개라면  <ul>
<li>어떤 학생은 문을 열고,  </li>
<li>다른 학생은 문을 닫고,  </li>
<li>결국 교실이 엉망이 될 거예요</li>
</ul>
</li>
</ul>
<p>그래서 선생님이 이렇게 말합니다:</p>
<blockquote>
<p>“이 문은 오직 <strong>하나의 열쇠</strong>로만 열 수 있어야 해!”</p>
</blockquote>
<hr />
<p>이게 바로 <strong>싱글톤의 핵심 아이디어</strong>예요.<br />👉 <strong>“열쇠(=객체 인스턴스)는 하나만 만들고, 모두가 그걸 공유한다!”</strong></p>
<hr />
<br />

<h1 id="🛠기술적으로-접근하면">🛠기술적으로 접근하면</h1>
<p>자바에서 싱글톤을 구현한다는 건 이런 뜻입니다.</p>
<ul>
<li><p><strong>클래스(Class)</strong>: 객체를 만들기 위한 설계도 (예: ‘자동차 설계도’)</p>
</li>
<li><p><strong>인스턴스(Instance)</strong>: 그 설계도로 실제로 만들어진 객체 (예: ‘실제 자동차 한 대’)</p>
</li>
</ul>
<p>보통은 new 키워드로 여러 개 만들 수 있죠.
하지만 싱글톤에서는 그걸 막아버립니다.</p>
<br />


<p> <strong>💻코드로 보면</strong></p>
<pre><code>public class MasterKey {
    // 세상에 단 하나뿐인 열쇠를 담아둘 변수
    private static MasterKey instance;

    // 외부에서 new로 못 만들게 막기
    private MasterKey() {}

    // 열쇠 꺼내기 (없으면 만들고, 있으면 기존 거 반환)
    public static MasterKey getInstance() {
        if (instance == null) {
            instance = new MasterKey(); // 처음 한 번만 생성
        }
        return instance;
    }
}</code></pre><p><strong>👇사용 예시</strong></p>
<pre><code>MasterKey key1 = MasterKey.getInstance();
MasterKey key2 = MasterKey.getInstance();

System.out.println(key1 == key2); // true (같은 열쇠!)</code></pre><br />

<p><strong>✅실사용 예</strong></p>
<table>
<thead>
<tr>
<th>상황</th>
<th>예시</th>
</tr>
</thead>
<tbody><tr>
<td>DB 연결 관리자</td>
<td>데이터베이스 연결을 하나의 인스턴스로 관리</td>
</tr>
<tr>
<td>Logger</td>
<td>모든 로그 기록을 한 객체가 관리</td>
</tr>
<tr>
<td>Config Manager</td>
<td>설정값을 전역적으로 공유</td>
</tr>
<tr>
<td>Cache Manager</td>
<td>여러 곳에서 동일한 캐시에 접근해야 할 때</td>
</tr>
</tbody></table>
<br />

<hr />
<br />

<h1 id="🔎멀티스레드-환경에서-싱글톤">🔎멀티스레드 환경에서 싱글톤?</h1>
<p>만약 <strong>민준이와 수아가 동시에 열쇠를 만들려고 달려들면</strong>,
잠깐 사이에 두 개의 열쇠가 만들어질 수도 있습니다.
(→ 여러 스레드가 동시에 if (instance == null)을 통과하는 문제)</p>
<p>이건 <strong>“스레드 안전성(Thread-safety)”</strong> 문제입니다.
즉, 여러 작업(스레드)이 동시에 같은 코드를 실행할 때도
인스턴스가 단 하나만 유지되도록 보장해야 하는 상황이죠.</p>
<blockquote>
<p>이를 해결하려면, <strong>“문을 잠그듯(lock)”</strong> 코드를 보호해야 해요.
즉, <strong>“누가 열쇠를 만드는 중이면, 다른 사람은 잠깐 기다려!”</strong> 하는 구조를 만들어야 합니다.</p>
</blockquote>
<br />

<p><strong>✅멀티스레드 환경에서 싱글톤을 안전하게 만드는 주요 방법</strong></p>
<ul>
<li>synchronized 키워드로 잠금 걸기</li>
<li>Double-Checked Locking(이중 검사) 사용하기</li>
<li>정적 내부 클래스(Holder 패턴) 활용하기</li>
<li>Enum 싱글톤 사용하기</li>
</ul>
<hr />
<h3 id="1-synchronized--문을-잠그는-방식">1. synchronized — “문을 잠그는 방식”</h3>
<pre><code>public class SafeMasterKey {
    private static SafeMasterKey instance;
    private SafeMasterKey() {}

    public static synchronized SafeMasterKey getInstance() {
        if (instance == null) {
            instance = new SafeMasterKey();
        }
        return instance;
    }
}</code></pre><p>이 방식은 <strong>“한 번에 한 명만 열쇠를 만들게 허락하는 방법”</strong></p>
<blockquote>
<p><strong>장점:</strong> 구현이 아주 간단하고 완벽하게 안전합니다.
<strong>단점:</strong> 매번 잠금을 걸기 때문에, 열쇠를 자주 꺼내면 느려질 수 있습니다.
(비유하자면 “매번 문을 잠그고 여는 건 안전하지만 좀 답답한 상황”이에요.)</p>
</blockquote>
<br />


<h3 id="2-double-checked-locking--필요할-때만-잠그기">2. Double-Checked Locking — “필요할 때만 잠그기”</h3>
<pre><code>public class FastMasterKey {
    private static volatile FastMasterKey instance;
    private FastMasterKey() {}

    public static FastMasterKey getInstance() {
        if (instance == null) { // 첫 번째 검사 (락 없이)
            synchronized (FastMasterKey.class) {
                if (instance == null) { // 두 번째 검사 (락 안에서)
                    instance = new FastMasterKey();
                }
            }
        }
        return instance;
    }
}</code></pre><p><strong>“평소엔 문을 잠그지 않지만, 진짜 새 열쇠를 만들 때만 잠그는 방식”</strong></p>
<blockquote>
<p><strong>장점:</strong> 빠르고 안전 (락을 거의 안 걸어요)
volatile은 CPU 캐시 동기화 문제를 해결해주는 키워드예요.
<strong>단점:</strong> 코드가 조금 복잡해요.
(비유하자면 “대부분 문은 열려 있지만,새 열쇠를 만들 때만 잠깐 잠그는 방식”이에요.)</p>
</blockquote>
<br />

<h3 id="3-정적-내부-클래스-initialization-on-demand-holder">3. 정적 내부 클래스 (Initialization-on-demand holder)</h3>
<pre><code>public class HolderKey {
    private HolderKey() {}

    private static class Holder {
        private static final HolderKey INSTANCE = new HolderKey();
    }

    public static HolderKey getInstance() {
        return Holder.INSTANCE;
    }
}</code></pre><p><strong>“열쇠를 실제로 필요할 때만 만들고, 그 시점엔 자동으로 한 번만 생성되는 방식”</strong></p>
<blockquote>
<p><strong>장점:</strong> 게으른 초기화(Lazy) + 스레드 안전(Thread-safe) + 빠름
JVM이 클래스 로딩 시점에 자동으로 안전하게 관리해줍니다.
(비유하자면 “열쇠 설계도는 미리 준비해두지만,누군가 진짜 ‘열쇠 주세요’라고 말할 때만 열쇠를 만드는 것”이에요.)</p>
</blockquote>
<br />

<h3 id="4-enum-싱글톤--자바가-보장하는-완벽한-방법">4. Enum 싱글톤 — “자바가 보장하는 완벽한 방법”</h3>
<pre><code>public enum MasterKey {
    INSTANCE;
}</code></pre><p>JVM이 클래스 로딩 시 단 한 번만 생성하므로
스레드 안전, 직렬화 문제, 리플렉션 공격까지 모두 해결됩니다.</p>
<blockquote>
<p><strong>단점:</strong> Enum이라는 형태가 어색하게 느껴질 수 있어요.
(비유하자면 “국가에서 공식적으로 인증한 열쇠 한 개만 존재하는 상황”이에요.)</p>
</blockquote>
<br />

<p><strong>📊싱글톤 적용법 표로 보기</strong></p>
<table>
<thead>
<tr>
<th>방법</th>
<th>안전성</th>
<th>성능</th>
<th>특징</th>
</tr>
</thead>
<tbody><tr>
<td>synchronized</td>
<td>✅ 안전</td>
<td>🐢 느림</td>
<td>간단하지만 매번 락</td>
</tr>
<tr>
<td>Double-Checked Locking</td>
<td>✅ 안전</td>
<td>⚡ 빠름</td>
<td>실무에서 자주 사용</td>
</tr>
<tr>
<td>Holder 패턴</td>
<td>✅ 안전</td>
<td>⚡ 빠름</td>
<td>JVM 로딩 규칙 이용</td>
</tr>
<tr>
<td>Enum</td>
<td>✅ 완벽</td>
<td>⚡ 빠름</td>
<td>가장 견고한 방법</td>
</tr>
</tbody></table>
<br />

<h3 id="💬-한-줄-요약">💬 한 줄 요약</h3>
<blockquote>
<p>“<strong>멀티스레드 환경</strong>에서는,
여러 사람이 동시에 열쇠를 만들려 해도
<strong>딱 하나의 열쇠만 만들어지도록 잠금(lock)이나 안전 장치를 두는 것이 핵심</strong>이에요.” 🔑</p>
</blockquote>