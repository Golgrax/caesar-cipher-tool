Ceasar Cipher Tool
=================

This project combines a Caesar Cipher cryptographic tool with an my interactive visualization skills, all served as a single-page web application using Flask.

Features
--------

### Caesar Cipher Tool (Center Panel)

*   Encrypt and decrypt alphabetic messages (spaces are preserved).
*   User-specified shift value ranging from 1 to 25.
*   Real-time input validation and clear error messages.
*   Convenient "Copy to Clipboard" functionality for the processed text.
*   A sleek, space-themed interface designed for usability.


### Application Structure (Layout)

*   **Left Panel**: Displays this project overview.
*   **Center Panel**: Hosts the interactive Caesar Cipher tool.
*   **Right Panel**: Features the live 3D "Cosmic Commits" visualization.

Technologies Used
-----------------

*   **Python (Flask)**: Serves the single-page application.
*   **HTML, CSS, JavaScript**: Structure, style, and client-side logic.
*   **Three.js**: Powers the 3D graphics for the globe, particles, arcs, and towers.
*   **Anime.js**: Used for sophisticated animations of 3D elements and UI transitions.

How to Get
----------

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Golgrax/caesar-cipher-tool.git
   ```

2. **Change into the project directory**

   ```bash
   cd caesar-cipher-tool
   ```
3. **(Optional) Inspect the code**
   Open the folder in your editor of choice:

   ```bash
   code .
   ```
4. **Verify Python version**
   Make sure you’re running Python 3.7 or newer:

   ```bash
   python3 --version
   ```

How to Run
----------

1. **Create a virtual environment**  
   ```bash
   python3 -m venv venv
   ```

2. **Activate the virtual environment**

   * On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```
   * On Windows (PowerShell):

     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
3. **Install dependencies**

   ```bash
   pip install Flask
   ```
4. **Run the application**

   ```bash
   python main.py
   # or
   python3 main.py
   ```
5. **Open in your browser**
   Navigate to `http://127.0.0.1:5000/` to see the app in action.

* * *

_This project overview is embedded directly into the application._