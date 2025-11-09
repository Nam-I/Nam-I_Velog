<h1 id="dfs와-bfs">DFS와 BFS</h1>
<ul>
<li><span style="background-color: skyblue;">Silver 2</span></li>
</ul>
<h1 id="✔-문제">✔ 문제</h1>
<blockquote>
<p>그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.</p>
</blockquote>
<h1 id="✔-입력">✔ 입력</h1>
<blockquote>
<p>첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.</p>
</blockquote>
<h1 id="✔-출력">✔ 출력</h1>
<blockquote>
<p>첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.</p>
</blockquote>
<pre><code>// 백준 1260.S2.DFS와 BFS - java 풀이
/**
 * ## 핵심 내용
 * - DFS 는 보통 재귀, stack
 * - BFS 는 queue
 * - 이 문제에서 DFS 부분을 stack 으로도 풀 수 있다.
 */

import java.util.*;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.util.Queue;

public class Main{

    static int N, M, V;
    static int[][] arr;
    static boolean[] visited;
    static Queue&lt;Integer&gt; q = new LinkedList&lt;&gt;();
    static StringBuilder sb = new StringBuilder();

    public static void main (String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st;

        st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        V = Integer.parseInt(st.nextToken());

        arr = new int[N + 1][N + 1];
        visited = new boolean[N + 1];

        for (int i = 0; i &lt; M; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());

            arr[start][end] = arr[end][start] = 1;

        }

        dfs(V);
        sb.append(&quot;\n&quot;);

        visited = new boolean[N + 1];

        bfs();

        bw.write(sb.toString() + &quot;\n&quot;);
        bw.flush();
        bw.close();
        br.close();
    }

    public static void dfs(int start){
        visited[start] = true;
        sb.append(start + &quot; &quot;);

        for (int i = 1; i &lt;= N; i++) {
            if (arr[start][i] == 1 &amp;&amp; !visited[i]){
                dfs(i);
            }
        }
    }

    public static void bfs(){
        q.offer(V);
        visited[V] = true;

        int curNode;

        while(!q.isEmpty()){

            curNode = q.poll();
            sb.append(curNode + &quot; &quot;);

            for (int i = 1; i &lt;= N; i++) {
                if(arr[curNode][i] == 1 &amp;&amp; !visited[i]){
                    q.offer(i);
                    visited[i] = true;
                }
            }
        }
    }

}</code></pre>