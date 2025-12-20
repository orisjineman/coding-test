public class DfsRecursion {
    // 출처: https://codingnojam.tistory.com/44
    // 예시 이미지: https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FcbRnry%2Fbtq2Ma1f8bm%2FpcMvcQhqVaIrmnHvCFzIC1%2Fimg.png

    // 방문 처리에 사용 할 배열 선언
    static boolean[] vistied = new boolean[9];

    // 예시 그래프의 연결 상태를 2차원 배열로 표현
    // 0번 인덱스는 아무 것도 없는 상태
    // index가 노드 번호와 매칭된다. (1번 인덱스는 1번 노드, 2번 인덱스는 2번 노드)
    static int[][] graph = {{}, {2,3,8}, {1,6,8}, {1,5}, {5,7}, {3,4,7}, {2}, {4,5}, {1,2}};

    public static void main(String[] args) {
        dfs(1);
    }

    static void dfs(int nodeIndex) {
        // 방문 처리
        vistied[nodeIndex] = true;

        // 방문 노드 출력
        System.out.print(nodeIndex + " -> ");

        // 방문한 노드에 인접한 노드 찾기
        for (int node : graph[nodeIndex]) {
            // 인접한 노드가 방문한 적이 없다면 DFS 수행
            if(!vistied[node]) {
                dfs(node);
            }
        }
    }
}
