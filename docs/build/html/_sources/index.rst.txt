============
Using Sphinx 
============

This document is a small test and also a little tutorial 
that can help you easily generate beatifull documents
using some parameters shown bellow.  

   
Presentation
============
learn using sphinx to simply generate documentation can save you a lot of time 
and you'll find in this page command line that I used to make it looks like this.
Sphinx use a syntax type called *RetructuredText*. `Here <https://thomas-cokelaer.info/tutorials/sphinx/rest_syntax.html>`_ you can learn more about this syntax. 

Usefull Parameters
=====================


.. toctree::
   :maxdepth: 2
   :caption: Contents:

* Warnings
.. warning::
   use parameter ".. warning:: " to create a warning like this.
   

   
* Lists
You can use several types of lists in your documents.
   * This is a bulleted list.
   1. this is a numbered list.
   #. this is also a numbered list.



Prerequisites
=============
As We are using python as default langage for ReadTheDocs, there are some requirements and dependencies to instal using pip.

1. Install **Sphinx** using **pip**: 

.. code-block:: python

   pip install Sphinx
2. Make sure you have **python** version 3x or 2x installed.

#. install **sphinx_rtd_theme** using **pip**:

   this is a global css template for ReadTheDocs. In my case I had to import it in **conf.py** but usually it is the default template used once you build your document.
   
.. code-block:: python

   pip install sphinx_rtd_theme

Continuous_Documentation
========================
When importing a new project on **ReasTheDocs**, a new Webhook should be created in your GIT repository to notify **ReadTheDoc** after each event.
We build and generate documentation in our case when a commit is done on the default branch **master**  


Revisions_Management
====================
**ReadTheDocs** affects a revision named *latest* when you import a GIT repository, But You can create another revision by adding a tag on your commit.

.. important::
   **ReadTheDocs** does not automatically display tags when generating the document, you might have to select tags to activate from the section **Version** and choose **Public** as *Confidentiality level*.