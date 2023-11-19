# Browser-History-Tracker-with-Doubly-Linked-List

**Overview**
<br>
This project implements a browser history tracker using a doubly linked list (DLL) in Python. It efficiently manages web page navigation history, including functionalities to visit new URLs, navigate backward and forward through the history, and handle "bad" websites as identified by a predefined set of rules.

<br>

**Features**
1. Doubly Linked List: Custom implementation of a DLL to store browsing history.
2. Navigation Controls: Functions to visit new URLs and navigate backward and forward through the history.
3. Bad Site Filtering: Integration with a metrics_api function to skip "bad" websites based on a predefined set of URLs.
4. Efficient History Management: Maintains current position in the history for quick access to adjacent sites.
5. Robust URL Handling: Ensures accurate tracking of URLs visited, including cases of revisiting the same URL.

<br>

**Usage**
<br>
1. Initialization: Create a BrowserHistory object with a homepage URL.
2. Visiting URLs: Use visit method to add new URLs to the history.
3. Navigating History: Apply backward and forward methods to move through the history.
4. Current URL: Use get_current_url to retrieve the currently viewed URL.
5. Handling Bad Sites: Automatically skips over URLs flagged by metrics_api.

<br>

**Requirements**
<br>
Python 3.x

<br>

**Ideal for**
<br>
Educational purposes for understanding DLLs in Python.
<br>
Web browser simulation projects.
<br>
Developers looking for custom implementations of history tracking in applications.
