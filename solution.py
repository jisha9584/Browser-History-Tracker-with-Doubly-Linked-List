"""
Project 2
CSE 331 F23 (Onsay)
Authored By: Hank Murdock
Originally Authored By: Andrew McDonald & Alex Woodring & Andrew Haas & Matt Kight & Lukas Richters & Sai Ramesh
solution.py
"""

from typing import TypeVar, List

# for more information on type hinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
Node = TypeVar("Node")  # represents a Node object (forward-declare to use in Node __init__)


# pro tip: PyCharm auto-renders docstrings (the multiline strings under each function definition)
# in its "Documentation" view when written in the format we use here. Open the "Documentation"
# view to quickly see what a function does by placing your cursor on it and using CTRL + Q.
# https://www.jetbrains.com/help/pycharm/documentation-tool-window.html


class Node:
    """
    Implementation of a doubly linked list node.
    Do not modify.
    """
    __slots__ = ["value", "next", "prev", "child"]

    def __init__(self, value: T, next: Node = None, prev: Node = None, child: Node = None) -> None:
        """
        Construct a doubly linked list node.

        :param value: value held by the Node.
        :param next: reference to the next Node in the linked list.
        :param prev: reference to the previous Node in the linked list.
        :return: None.
        """
        self.next = next
        self.prev = prev
        self.value = value

        # The child attribute is only used for the application problem
        self.child = child

    def __repr__(self) -> str:
        """
        Represents the Node as a string.

        :return: string representation of the Node.
        """
        return f"Node({str(self.value)})"

    __str__ = __repr__


class DLL:
    """
    Implementation of a doubly linked list without padding nodes.
    Modify only below indicated line.
    """
    __slots__ = ["head", "tail", "size"]

    def __init__(self) -> None:
        """
        Construct an empty doubly linked list.

        :return: None.
        """
        self.head = self.tail = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        result = []
        node = self.head
        while node is not None:
            result.append(str(node))
            node = node.next
        return " <-> ".join(result)

    def __str__(self) -> str:
        """
        Represent the DLL as a string.

        :return: string representation of the DLL.
        """
        return repr(self)

    # MODIFY BELOW #

    def empty(self) -> bool:
        """
        Check if the Doubly Linked List (DLL) is empty.
        This method returns True if the DLL is empty, i.e., it contains no elements.
        Otherwise, it returns False.
        Returns: bool: True if the DLL is empty, else False.
        """
        return self.head is None

    def push(self, val: T, back: bool = True) -> None:
        """
        Add a node containing 'val' to the back (or front) of the Doubly Linked List (DLL) and update the size
        accordingly.
        This method allows you to add a new node with the value 'val' to either the back or front of the DLL, depending
        on the 'back' parameter. By default, it adds 'val' to the back of the DLL.
        Parameters:
            val (T): The value to be added to the DLL.
            back (bool, optional): If True, add 'val' to the back of the DLL; if False, add it to the front. Default is
            True.
        Returns: None
        """
        new_node = Node(val)  # Create a new node with the given value

        if back:
            # Adding to the back of the DLL
            if self.tail is None:
                # If the DLL is empty, set both head and tail to the new node
                self.head = self.tail = new_node
            else:
                # Update the next pointer of the current tail node
                self.tail.next = new_node
                # Update the previous pointer of the new node
                new_node.prev = self.tail
                # Update the tail to the new node
                self.tail = new_node
        else:
            # Adding to the front of the DLL
            if self.head is None:
                # If the DLL is empty, set both head and tail to the new node
                self.head = self.tail = new_node
            else:
                # Update the previous pointer of the current head node
                self.head.prev = new_node
                # Update the next pointer of the new node
                new_node.next = self.head
                # Update the head to the new node
                self.head = new_node

        # Increment the size of the DLL
        self.size += 1

    def pop(self, back: bool = True) -> None:
        """
        Remove a node from the back (or front) of the Doubly Linked List (DLL) and update the size accordingly.
        This method allows you to remove a node either from the back or front of the DLL, depending on the 'back'
        parameter.
        If the DLL is empty, the method does nothing.
        Parameters: back (bool, optional): If True, remove a node from the back of the DLL; if False, remove it from the
        front. Default is True.
        Returns: None
        """
        if self.head is None:
            # If the DLL is empty, do nothing
            return

        if back:
            # Removing from the back of the DLL
            if self.head == self.tail:
                # If there's only one node in the DLL, set both head and tail to None
                self.head = self.tail = None
            else:
                # Update the tail to its previous node
                self.tail = self.tail.prev
                # Set the next pointer of the new tail to None
                self.tail.next = None
        else:
            # Removing from the front of the DLL
            if self.head == self.tail:
                # If there's only one node in the DLL, set both head and tail to None
                self.head = self.tail = None
            else:
                # Update the head to its next node
                self.head = self.head.next
                # Set the previous pointer of the new head to None
                self.head.prev = None

            # Decrement the size of the DLL
        self.size -= 1

    def list_to_dll(self, source: List[T]) -> None:
        """
        Create a Doubly Linked List (DLL) from a standard Python list and replace the existing DLL with the new one.
        This method constructs a DLL from the provided 'source' list. If there are already nodes in the DLL, it will
        clear the existing DLL and replace it with the new one created from 'source'.
        Parameters: source (list[T]): Standard Python list from which to construct the DLL.
        Returns: None
        """
        self.head = self.tail = None
        self.size = 0

        # Iterate over each item in the source list and create a new node for each item
        for item in source:
            new_node = Node(item)

            if self.head is None:
                # If the DLL is empty, set both head and tail to the new node
                self.head = self.tail = new_node
            else:
                # Update the next pointer of the current tail node
                self.tail.next = new_node
                # Update the previous pointer of the new node
                new_node.prev = self.tail
                # Update the tail to the new node
                self.tail = new_node

            # Increment the size of the DLL
            self.size += 1
    def dll_to_list(self) -> List[T]:
        """
        Create a standard Python list from a Doubly Linked List (DLL).
        This method constructs a standard Python list containing the values of the nodes in the DLL.
        Returns: list[T]: A Python list containing the values of the nodes in the DLL.
        """
        values = []  # Initialize an empty list to store the values

        # Iterate over each node in the DLL and append its value to the list
        current_node = self.head
        while current_node is not None:
            values.append(current_node.value)
            current_node = current_node.next

        return values

    def _find_nodes(self, val: T, find_first: bool = False) -> List[Node]:
        """
        Create a list of Node objects in the Doubly Linked List (DLL) with the value 'val'.
        This method constructs a list of Node objects representing all instances (or the first instance, if 'find_first'
        is True) of the specified 'val' in the DLL.
        Parameters:
            val (T): The value to be found in the DLL.
            find_first (bool, optional): If True, find only the first instance of 'val' in the DLL; if False, find all
            instances. Default is False.
        Returns:
            List[Node]: A list of Node objects representing nodes in the DLL with the value 'val'. Returns an empty list
            if 'val' is not found.
        """
        result = []  # Initialize an empty list to store matching nodes

        # Iterate over each node in the DLL
        current_node = self.head
        while current_node is not None:
            if current_node.value == val:
                result.append(current_node)
                if find_first:
                    break  # If find_first is True, break after finding the first occurrence
            current_node = current_node.next

        return result

    def find(self, val: T) -> Node:
        """
        Find the first Node object in the Doubly Linked List (DLL) with the value 'val'.
        This method calls the '_find_nodes' method to search for the first instance of the specified 'val' in the DLL
        and returns the associated Node object.
        Parameters: val (T): The value to be found in the DLL.
        Returns: Node: The first Node object in the DLL whose value is 'val', or None if 'val' is not found.
        """
        # Call the _find_nodes method with find_first=True to find the first occurrence
        matching_nodes = self._find_nodes(val, find_first=True)

        # Return the first matching node if it exists, otherwise return None
        return matching_nodes[0] if matching_nodes else None

    def find_all(self, val: T) -> List[Node]:
        """
        Find all Node objects in the Doubly Linked List (DLL) with the value 'val' and return them in a standard Python
        list.
        This method calls the '_find_nodes' method to search for all instances of the specified 'val' in the DLL and
        returns a standard Python list containing the associated Node objects.
        Parameters: val (T): The value to be found in the DLL.
        Returns: list[Node]: A standard Python list containing all Node objects in the DLL whose value is 'val', or an
        empty list if 'val' is not found.
        """
        # Call the _find_nodes method with find_first=False to find all occurrences
        matching_nodes = self._find_nodes(val, find_first=False)

        # Return the list of matching nodes (may be empty)
        return matching_nodes

    def _remove_node(self, to_remove: Node) -> None:
        """
        Remove a specified Node from the Doubly Linked List (DLL) given a reference to that node.
        This method removes the provided 'to_remove' Node from the DLL.
        Parameters: to_remove (Node): The Node to be removed from the DLL.
        Returns: None
        """
        if to_remove is not None:
            # Update the next node's previous reference if it exists
            if to_remove.next is not None:
                to_remove.next.prev = to_remove.prev

            # Update the previous node's next reference if it exists
            if to_remove.prev is not None:
                to_remove.prev.next = to_remove.next

            # Update DLL head and tail if necessary
            if self.head == to_remove:
                self.head = to_remove.next
            if self.tail == to_remove:
                self.tail = to_remove.prev

            # Decrement the DLL size
            self.size -= 1

    def remove(self, val: T) -> bool:
        """
        Remove the first Node in the Doubly Linked List (DLL) with the value 'val'.
        This method uses the 'find' method to locate the first instance of the specified 'val' in the DLL,
        then calls the '_remove_node' method to remove that Node.
        Parameters: val (T): The value to be removed from the DLL.
        Returns: bool: True if a Node with 'val' was found and removed, else False.
        """
        # Find the first occurrence of the value val in the DLL
        node_to_remove = self.find(val)

        # If the node with the value val exists, remove it and return True
        if node_to_remove is not None:
            self._remove_node(node_to_remove)
            return True

        # If the value val was not found, return False
        return False

    def remove_all(self, val: T) -> int:
        """
        Remove all Node objects in the Doubly Linked List (DLL) with the value 'val'.
        This method uses the 'find_all' method to locate all instances of the specified 'val' in the DLL,
        then calls the '_remove_node' method for each found instance to remove those Nodes.
        Parameters: val (T): The value to be removed from the DLL.
        Returns: int: The number of Node objects with 'val' that were found and removed.
        """
        # Find all occurrences of the value val in the DLL
        nodes_to_remove = self.find_all(val)

        # Remove each matching node using _remove_node and count the number of removals
        removal_count = 0
        for node_to_remove in nodes_to_remove:
            self._remove_node(node_to_remove)
            removal_count += 1

        # Return the number of nodes removed
        return removal_count

    def reverse(self) -> None:
        """
        Reverse the Doubly Linked List (DLL) in-place by modifying next and prev references of Node objects.
        This method reverses the order of Node objects in the DLL without creating a new DLL.
        It updates the 'self.head' and 'self.tail' references accordingly.
        Returns: None
        """
        current_node = self.head
        prev_node = None

        # Iterate through the DLL, swapping next and prev references for each node
        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            current_node.prev = next_node

            # Move to the next node
            prev_node = current_node
            current_node = next_node

        # Swap self.head and self.tail to reflect the new head and tail of the reversed DLL
        self.head, self.tail = self.tail, self.head

class BrowserHistory:

    def __init__(self, homepage: str):
        """
        Initialize the BrowserHistory object with a specified homepage.
        This method sets up the BrowserHistory object and ensures that if 'get_current_url' is called immediately after
        initialization, it returns the provided 'homepage'. The object is ready to track the current web page.
        Parameters: homepage (str): The URL of the homepage.
        Returns: None
        """
        # Create a doubly linked list (DLL) to store the browsing history
        self.history = DLL()

        # Visit the homepage and add it to the history
        self.history.push(homepage)

        # Maintain a reference to the current node
        self.current_node = self.history.head  # Initialize it with the homepage node

    def get_current_url(self) -> str:
        """
        Get the URL that the browser is currently on.
        This method returns the URL of the current web page that has been set through the most recent 'visit'
        operation or any sequence of backward and forward operations.
        Returns: str: The URL of the current web page.
        """
        # Simply call the get_current_url method of the DLL object
        return self.current_node.value

    def visit(self, url: str) -> None:
        """
        Visit the specified URL and update the browser's history accordingly.
        This method sets the current web page to the provided 'url' and ensures that if 'get_current_url'
        is called immediately afterward, it returns the 'url'. It also updates the forward history such that
        'url' becomes the next page in the forward history, and all previous forward history is deleted.
        Parameters: url (str): The URL to visit.
        Returns: None
        """
        new_node = Node(url)

        while self.current_node != self.history.tail:
            self.history.pop()

        # Update the current node and URL
        self.current_node = new_node
        self.current_node.prev = self.history.tail

        # Insert the new node after the current node
        if self.history.head is None:
            # If the history is empty, make the new node both head and tail
            self.history.head = self.history.tail = new_node
        else:
            # Otherwise, insert the new node after the current node
            self.history.tail.next = new_node
            self.history.tail = new_node
    
    def backward(self) -> None:
        """
        Navigate to the previous page in the browser's history, skipping over any "bad" sites as defined by the
        metrics_api function.
        This method moves the browser to the previous page in the history, provided there is a previous page.
        It skips over any "bad" sites as defined by the 'metrics_api' function. The homepage is guaranteed to be a good
        site.
        Returns: None
        """
        if self.history.head.prev is None:
            current_node = self.history.head
            # If the history is empty or has only one page, do nothing or stay on the current page

        # Start from the current page and move backward in history
        current_node = self.current_node

        # Iterate through the history list to find the previous good site
        while current_node.prev is not None:
            current_node = current_node.prev
            if not metrics_api(current_node.value):
                # If the current node is not a bad site, update the current URL
                self.current_node = current_node
                break

    def forward(self) -> None:
        """
        Visit the page ahead of the current one in history, skipping over "bad" sites.
        This method navigates to the page ahead of the current one in the browser's history,
        provided there is a good page. It skips over any "bad" sites as defined by the 'metrics_api' function.
        If there is no good page ahead of the current page in history or if the current page is the most recent,
        the browser stays on the current page.
        Returns: None
        """

        current_node_n = self.current_node.next

        if current_node_n is None:
            return

        while metrics_api(current_node_n.value):
            current_node_n = current_node_n.next
            if current_node_n is None:
                return
        self.current_node = current_node_n

# DO NOT MODIFY
intervention_set = set(['https://malicious.com', 'https://phishing.com', 'https://malware.com'])
def metrics_api(url: str) -> bool:
    """
    Uses the intervention_set to determine what URLs are bad and which are good. 

    :param url: The url to check.
    :returns: True if this is a malicious website, False otherwise.
    """
    if url in intervention_set:
        return True
    return False


