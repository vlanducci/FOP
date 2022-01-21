.. FOP documentation master file, created by
   sphinx-quickstart on Fri Jan 21 19:29:49 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to FOP's documentation!
===============================

**Bold**

*Italic*

.. note::
   Box

.. image is showing error but it actually works dont worry, same with code block
.. image:: /ReadTheDocsImages/Bingus.jpg


Testing code block:

.. code-block:: python

   output = "Hello World"
   print(output)

.. there are other ways of doing tabels but just search them up

========== ========== ==========
Header 1   Header 2   Header 3
========== ========== ==========
contents 1 contents 2 contents 3
contents 4 contents 5 contents 6
contents 7 contents 8 contents 9
========== ========== ==========

.. list-table:: Table Test 2
   :widths: 30 30 30
   :header-rows: 1
   :class: tight_table

   * - Header 1
     - Header 2
     - Header 3
   * - contents 1
     - contents 2
     - contents 3
   * - contents 4
     - contents 5
     - contents 6
   * - contents 7
     - contents 8
     - contents 9

.. :hidden: hides table of contents
.. If it is freaking out then just delete html file and re-make it

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Test

   README.rst
   test.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Practicals

   Prac01/README.rst
   Prac02/README.rst
   Prac03/README.rst
   Prac04/README.rst
   Prac05/README.rst
   Prac06/README.rst
   Prac07/README.rst
   Prac08/README.rst
   Prac09/README.rst
   Prac10/PresentingData/README.rst
   Prac11/README.rst
   Assigments/Assigment1/FOP_Assignment_20769446/README.rst

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Tests

   Tests/FinalExam/FOP_Final_20769446/README.rst
   Tests/PracTest1/README.rst
   Tests/PracTest2/README.rst
   Tests/PracTest3/README.rst
   Tests/PracTest4/README.rst
   Tests/PracTest5/README.rst