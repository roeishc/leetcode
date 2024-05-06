/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class RemoveNodesFromLinkedList {
    public static ListNode removeNodes(ListNode head) {
        ListNode temp = head;
        MonotonicStackDecreasing stack = new MonotonicStackDecreasing();
        while (temp != null){
            stack.push(temp);
            temp = temp.next;
        }
        if (stack.isEmpty())
            return null;
        ListNode newHead = stack.pop();
        while (!stack.isEmpty()){
            temp = stack.pop();
            temp.next = newHead;
            newHead = temp;
        }
        return newHead;
    }

public static class MonotonicStackDecreasing {

        private final Deque<ListNode> stack;

        public MonotonicStackDecreasing(){
            this.stack = new ArrayDeque<>();
        }

        public ListNode push(ListNode node){
            ListNode temp = node;
            while (!stack.isEmpty() && stack.peekFirst().val < node.val)
                temp = stack.pop();
            stack.addFirst(node);
            return temp;
        }

        public ListNode pop(){
            return stack.pop();
        }

        public ListNode peek(){
            if (stack.isEmpty())
                return null;
            return stack.peekFirst();
        }

        public boolean isEmpty(){
            return stack.isEmpty();
        }
    }
}