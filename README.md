# PYQ Analyzer using Machine Learning

## Overview

PYQ Analyzer is a Python-based tool developed to assist students in
preparing efficiently for examinations by analyzing Previous Year
Questions (PYQs). The system extracts questions from PDF documents,
evaluates their importance using machine learning techniques, and
estimates the time required to study each question. By combining
automation with intelligent prioritization, the project aims to simplify
the exam preparation process.

## Problem Statement

Students often struggle to identify important questions from large
volumes of study material and previous year papers. This process is
typically manual, time-consuming, and inconsistent, which leads to
inefficient preparation and increased stress during exams.

## Solution

The proposed system automates the analysis of PYQs by extracting
questions directly from PDFs and allowing users to input key features
such as marks and frequency. Based on this input, a machine learning
model classifies the importance of each question, while a heuristic
formula estimates the required study time. The system also supports
saving and loading of data, enabling students to reuse previous analysis
without repeating manual effort.

## Features

The application supports multiple subjects, allowing users to manage
different datasets within a single system. It performs automatic
extraction of questions from PDF files and uses machine learning for
classifying them into priority categories such as study, revise, or
skip. Additionally, it estimates study time for each question and
provides a simple command-line interface for easy interaction. The
system also includes a data persistence feature that allows users to
save and reload previously analyzed data.

## How It Works

The user begins by uploading a PDF containing questions. The system
extracts and displays each question, prompting the user to enter marks
and frequency values. These inputs are used by the machine learning
model to determine the priority of each question. A time estimation
formula is then applied to calculate the approximate study time. The
analyzed data is stored locally, allowing users to reload and review
their results at any time.

## Tech Stack

The project is implemented using Python and utilizes libraries such as
pypdf for PDF processing, scikit-learn for machine learning, and pandas
for data handling. These tools collectively enable efficient data
extraction, processing, and prediction.

## Project Structure

The project is organized into modular components including the main
execution file, utility modules for PDF handling, machine learning
logic, and data storage. Additional directories are used to manage
datasets and input PDFs, ensuring a clean and maintainable structure.

## Installation

To run the project, download the project files and open the folder in
your system. Install the required dependencies using the requirements
file by running the appropriate command in the terminal. This ensures
that all necessary libraries are available for execution.

## How to Run

1. Install dependencies:
   pip install -r requirements.txt

2. Run:
   python main.py

## Usage

The application is executed through the main Python file. Once started,
the user is presented with a menu that allows them to upload and analyze
PDFs, load previously saved data, view important questions, and check
total study time. The system is designed to be simple and user-friendly.

## Data Source

The questions and dataset used in this project are derived from course
materials, lecture notes, and module content, ensuring realistic and
relevant academic patterns across multiple subjects.

## Future Improvements

Future enhancements may include automatic extraction of marks directly
from PDFs, improved natural language processing for better question
understanding, development of a graphical user interface, and
integration of advanced recommendation systems.

## Conclusion

This project demonstrates how machine learning and logical
decision-making can be effectively combined to solve a real-world
academic problem. By automating the analysis of previous year questions,
the system provides a practical and scalable solution for improving exam
preparation strategies.
