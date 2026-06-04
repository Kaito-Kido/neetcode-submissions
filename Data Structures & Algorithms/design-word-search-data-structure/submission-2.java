class WordDictionary {
    private TrieNode root;

    public WordDictionary() {
        root = new TrieNode();
    }

    public void addWord(String word) {
        TrieNode node = root;
        for (Character c : word.toCharArray()) {
            node = node.children.computeIfAbsent(c, k -> new TrieNode());
        }

        node.isWord = true;
    }

    public boolean search(String word) {
        return findWord(word, root);
    }

    private boolean findWord(String word, TrieNode node) {
        for (int i = 0; i <  word.length(); i++) {
            Character c = word.charAt(i);
            if (c == '.') {
                boolean finded = false;
                for (TrieNode childNode : node.children.values()) {
                    finded = findWord(word.substring(i + 1, word.length()), childNode);
                    if (finded) return true;
                }
                return finded;
            } else {
                TrieNode current = node.children.get(c);
                if (current == null)
                    return false;
                node = current;
            }
        }

        return node != null && node.isWord;
    }

        private static class TrieNode {
        public HashMap<Character, TrieNode> children = new HashMap<>();
        public boolean isWord;
    }
}
