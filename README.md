# 🖌️ Random Street Artist

This project's aim was to teach us modularity in Python, I made it back when I was 16. Every part of a building (floors, door, windows, roof) is drawn by its own function, then randomly combined.It draws 4 randomly generated buildings using the turtle Python module. Every aspect of the building is randomized — no two runs ever look the same.

## 🎲 Randomized elements

Each run draws **4 randomly generated buildings**, where almost every visual detail is randomized:

| Element           | Variations                |
| ----------------- | ------------------------- |
| 🏢 Floors         | 1 to 5                    |
| 🎨 Building color | Random color              |
| 🚪 Door style     | Squared or rounded        |
| 📍 Door position  | Random along the facade   |
| 🟫 Door color     | Random color              |
| 🪟 Windows        | Regular window or balcony |
| 🏠 Roof style     | Triangular or flat        |

## How to run

```bash
python3 -m street_artist
```

## 🧩 How it's structured

The drawing logic is split across one module per concern, each holding small single-purpose functions, all drawing through the primitives in `base.py`:

```
street_artist/
├── __main__.py
├── street.py
├── floors.py
├── facade.py
├── roofs.py
├── ground.py
└── base.py
```

Each function handles one job and takes randomized parameters, which is what makes every building unique while keeping the code easy to follow and extend.
