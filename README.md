# Helldivers 2 Easy Stratagems

A simple tool to quickly execute stratagems in *Helldivers 2*. Press a hotkey, and the app automatically inputs the correct stratagem sequence in the game.

## Features
- **Quick stratagem execution** – Select a stratagem from the UI and activate it with a single key.
- **Customizable UI** – Choose stratagems from your current loadout via drop-down menus.

## Hotkeys
Default keybinds for every drop-down menu:

- **O** → Drop-down 1
- **P** → Drop-down 2
- **[** → Drop-down 3
- **]** → Drop-down 4

You will be able to change these in future updates (I hope there will be some).



## Installation & Usage
1. Clone the repository:
   ```sh
   git clone https://github.com/T1nG3R/EasyStratagems.git
   cd EasyStratagems
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. **Configure in-game key bindings:**  
   To ensure the program works correctly, go to:
   ```
   Options -> Mouse & Keyboard -> Change bindings -> Stratagem
   ```
   Set the bindings exactly as shown in the image:  
   ![Key Bindings](https://i.imgur.com/YemvTRL.png)

4. Run the application:
   ```sh
   python main.py
   ```

## TODO
- [ ] Change MainWindow title (i forgor 💀)
- [ ] Support for other hotkeys
- [ ] Add mission stratagems
- [ ] Improve UI layout (grid for dropdowns)
- [ ] Custom title bar
- [ ] Resize support (?)
- [ ] Build `.exe` for Windows

## Contribution
Feel free to fork this repository and suggest improvements.  
For any issues, create a GitHub issue or contact me.
