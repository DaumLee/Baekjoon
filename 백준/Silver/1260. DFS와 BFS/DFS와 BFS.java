import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {

    static StringBuilder sb = new StringBuilder();
    static boolean[] v;
    static int[][] arr;

    static int N, M, K;

    static Queue<Integer> q = new LinkedList<>();

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        StringTokenizer st = new StringTokenizer(br.readLine());
        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());
        K = Integer.parseInt(st.nextToken());

        arr = new int[N + 1][N + 1];
        v = new boolean[N + 1];

        for (int i = 0; i < M; i++) {
            StringTokenizer str = new StringTokenizer(br.readLine());

            int a = Integer.parseInt(str.nextToken());
            int b = Integer.parseInt(str.nextToken());

            arr[a][b] = arr[b][a] = 1;
        }
        dfs(K);
        sb.append("\n");
        v = new boolean[N + 1];
        bfs(K);
        System.out.println(sb);
    }

    public static void dfs(int K) {
        v[K] = true;
        sb.append(K + " ");
        for (int i = 0; i <= N; i++) {
            if (arr[K][i] == 1 && !v[i])
                dfs(i);
        }
    }

    public static void bfs(int K) {
        q.add(K);
        v[K] = true;

        while (!q.isEmpty()) {
            K = q.poll();
            sb.append(K + " ");
            for (int i = 1; i <= N; i++) {
                if (arr[K][i] == 1 && !v[i]) {
                    q.add(i);
                    v[i] = true;
                }
            }
        }
    }
}