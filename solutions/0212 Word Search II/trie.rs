use std::{collections::HashMap, fmt};

struct Node {
    name: char,
    sub_nodes: HashMap<char, Node>,
}

impl Node {
    fn new(name: char) -> Node {
        Node {
            name,
            sub_nodes: HashMap::new(),
        }
    }

    fn name(&self) -> char {
        self.name
    }

    fn add_sub_node(&mut self, node: Node) {
        if self.sub_nodes.get(&node.name()).is_some() {
            return;
        }
        self.sub_nodes.insert(node.name(), node);
    }

    fn exists(&self, name: char) -> bool {
        self.sub_nodes.get(&name).is_some()
    }

    fn print(&self) {
        if self.name != ' ' {
            print!("{}", self.name);
        }
        if self.sub_nodes.is_empty() {
            println!("");
        } else {
            for sub_node in self.sub_nodes.values() {
                sub_node.print();
            }
        }
    }
}

fn trie(mut root: Node, word: &str) -> Node {
    if word.is_empty() {
        return root;
    }
    let mut chars = word.chars();
    let name = chars.next().unwrap();
    let mut node = Node::new(name);
    node = trie(node, chars.as_str());
    root.add_sub_node(node);
    return root;
}

pub fn main() {
    let vv = vec!["you", "look", "book", "abc", "sss"];
    let mut root = Node::new(' ');
    for word in vv.iter() {
        root = trie(root, word);
    }

    root.print();
}
