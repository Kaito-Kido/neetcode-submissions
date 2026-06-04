class PrefixTree {
    private HashMap<Character, TrieNode> rootMap;

    public PrefixTree() {
        rootMap = new HashMap<Character, TrieNode>();
    }

    public void insert(String word) {
        int n = word.length();
        int index = 0;
        if (!rootMap.containsKey(word.charAt(index))) {
            rootMap.put(word.charAt(index), new TrieNode());
        }
        TrieNode currentNode = rootMap.get(word.charAt(index));
        if (index == n - 1) {
            currentNode.isWord = true;
        }
        index++;
        while (index < n) {
            Character current = word.charAt(index);
            if (!currentNode.subNodes.containsKey(current)) {
                currentNode.subNodes.put(current, new TrieNode());
            }

            if (index == n - 1) {
                currentNode.subNodes.get(current).isWord = true;
            }

            currentNode = currentNode.subNodes.get(current);
            index++;
        }
    }

    public boolean search(String word) {
        int index = 0;
        int n = word.length();
        if (!rootMap.containsKey(word.charAt(index))) return false;
        TrieNode currentNode = rootMap.get(word.charAt(index));
        if (index == n - 1 && !currentNode.isWord) return false;
        index++;
        while (index < n) {
            Character current = word.charAt(index);
            if (!currentNode.subNodes.containsKey(current)) return false;
            if (index == n - 1 && !currentNode.subNodes.get(current).isWord) return false;
            currentNode = currentNode.subNodes.get(current);
            index++;
        }

        return true;
    }

    public boolean startsWith(String prefix) {
        int index = 0;
        int n = prefix.length();
        if (!rootMap.containsKey(prefix.charAt(index))) return false;
        TrieNode currentNode = rootMap.get(prefix.charAt(index));
        index++;
        while (index < n) {
            Character current = prefix.charAt(index);
            if (!currentNode.subNodes.containsKey(current)) return false;
            currentNode = currentNode.subNodes.get(current);
            index++;
        }
        return true;
    }

    public class TrieNode {
        public HashMap<Character, TrieNode> subNodes = new HashMap<>();
        public boolean isWord = false; 
    }
}
