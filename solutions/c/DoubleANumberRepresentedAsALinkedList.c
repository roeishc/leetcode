/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* getNewNode(int val, struct ListNode* next);

struct ListNode* doubleIt(struct ListNode* head){
    
    if (!head)
        return NULL;

    struct ListNode* startPoint;

    if (head->val >= 5){
        head->next = getNewNode((head->val) * 2 % 10, head->next);
        head->val = 1;
        startPoint = head->next;
    }
    else{
        head->val *= 2;
        startPoint = head;
    }
    
    struct ListNode* temp, *prev;
    prev = startPoint;
    temp = startPoint->next;

    while (temp != NULL){

        if (temp->val >= 5){
            temp->val = temp->val * 2 % 10;
            prev->val += 1;
        }
        else
            temp->val *= 2;

        temp = temp->next;
        prev = prev->next;
    }

    return head;

}

struct ListNode* getNewNode(int val, struct ListNode* next){

    struct ListNode* newNode = (struct ListNode*)malloc(sizeof(struct ListNode));
    if (!newNode)
        return NULL;
    newNode->val = val;
    newNode->next = next;
    return newNode;

}