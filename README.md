# DJI Tello Drone Control with djitellopy

This repository demonstrates how to control a **DJI Tello drone** using Python and the **djitellopy** library.  
The drone is controlled via the DJI Tello SDK over UDP after connecting your computer directly to the drone’s Wi-Fi network.

---

## 📦 Requirements

- Python **3.8 – 3.12** (recommended)
- DJI **Tello** drone
- Wi-Fi adapter (to connect to the Tello network)
- OS: Windows / macOS / Linux

---

## 📥 Installation

Install the required Python library:

```bash
pip install djitellopy
```

---

## 📡 How the Connection Works

- The DJI Tello drone creates its **own Wi-Fi network**
- Your computer connects **directly** to this network
- Communication is handled using the **DJI Tello SDK** over **UDP**
- The `djitellopy` library abstracts the low-level SDK calls

To establish a connection, only **one function call** is required:

```python
tello.connect()
```

Once connected, you can send movement commands, read video frames, and access telemetry data.

---

## 🚀 Running the Drone Tasks

Each task file controls a specific drone behavior.

Example:

```bash
python part_x.py
```

Replace `part_x.py` with the task file you want to run (e.g. `part_1.py`, `part_2.py`, etc.).

Make sure:
- You are connected to the **Tello Wi-Fi**
- The drone battery is sufficiently charged
- No other device is controlling the drone

---

## 🧪 Example Workflow

1. Power on the DJI Tello drone
2. Connect your computer to the **Tello Wi-Fi**
3. Run the task file:
   python task_x.py
4. The drone will execute the programmed movement or behavior
5. The drone lands automatically or via code (depending on the task)

---

## 🛠 Troubleshooting

### ❌ AV / Video Stream Error

If you encounter this error when reading frames:

```bash
av.error.OSError: [Errno 10014] Error number -10014 occurred: 'udp://@0.0.0.0:11111'
```

This is a known compatibility issue with newer versions of the **PyAV** package.

### ✅ Fix: Reinstall a Compatible AV Version

```bash
pip uninstall av  
pip install "av<15"
```

Then run the task again:

```bash
python part_x.py
```
---

## ⚠️ Safety Notes

- Always test indoors in a **clear, open space**
- Keep hands away from propellers
- Be ready to manually land the drone if needed
- Use `tello.land()` in your scripts for safe shutdown

---

## 📚 References

- DJI Tello SDK Documentation  
- djitellopy GitHub Repository  