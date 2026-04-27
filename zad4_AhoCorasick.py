from collections import deque, defaultdict

class AhoCorasick:
    def __init__(self):
        self.trie = {}
        self.output = defaultdict(list)
        self.fail = {}

    def add_word(self, word):
        node = self.trie
        for char in word:
            if char not in node:
                node[char] = {}
            node = node[char]
        # zapisujemy końce wzorców
        node['_end_'] = True
        self.output[id(node)].append(word)

    def build(self):
        queue = deque()
        # ustawiamy funkcje fail dla poziomu 0
        for char, node in self.trie.items():
            self.fail[id(node)] = id(self.trie)
            queue.append(node)

        while queue:
            current_node = queue.popleft()
            for char, next_node in current_node.items():
                if char == '_end_':  # ignorujemy marker końca słowa
                    continue
                # przechodzenie funkcji fail
                fail_node = self.fail[id(current_node)]
                while fail_node != id(self.trie) and char not in self._node_by_id(fail_node):
                    fail_node = self.fail[fail_node]
                fail_node = self._node_by_id(fail_node).get(char, self.trie)
                self.fail[id(next_node)] = id(fail_node)
                # lączymy wyjścia
                self.output[id(next_node)].extend(self.output[id(fail_node)])
                queue.append(next_node)

    def search(self, text):
        results = []
        node = self.trie

        for i, char in enumerate(text):
            while node != self.trie and char not in node:
                node = self._node_by_id(self.fail[id(node)])
            node = node.get(char, self.trie)
            if id(node) in self.output:
                for pattern in self.output[id(node)]:
                    results.append((i - len(pattern) + 1, pattern))
        return results

    def _node_by_id(self, node_id):
        return {id(v): v for v in self._all_nodes(self.trie)}.get(node_id)

    def _all_nodes(self, node):
        yield node
        for child in node.values():
            if isinstance(child, dict):
                yield from self._all_nodes(child)


# Przykład użycia
if __name__ == "__main__":
    patterns = ["Ron", "ona", "aha", "aldo"]
    text = "Ronaldo"

    ac = AhoCorasick()
    for pattern in patterns:
        ac.add_word(pattern)
    ac.build()

    matches = ac.search(text)
    print("Dopasowania:")
    for pos, pattern in matches:
        print(f"Znaleziono '{pattern}' na pozycji {pos}")
