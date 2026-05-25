class Solution {
    public Node cloneGraph(Node node) {
        if (node == null) return null;

        Map<Integer, Node> valueToNodeMap = new HashMap<>();
        Queue<Node> q = new LinkedList<>();
        valueToNodeMap.put(node.val, new Node(node.val));
        q.add(node);
        while (q.size() != 0) {
            Node currentNode = q.poll();
            Node currentClonedNode = valueToNodeMap.get(currentNode.val);
            for (Node neighbor : currentNode.neighbors) {
                if (!valueToNodeMap.containsKey(neighbor.val)) {
                    valueToNodeMap.put(neighbor.val, new Node(neighbor.val));
                    q.add(neighbor);
                }
                currentClonedNode.neighbors.add(valueToNodeMap.get(neighbor.val));
            }
        }

        return valueToNodeMap.get(node.val);
    }
}