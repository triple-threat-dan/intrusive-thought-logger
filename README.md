# Intrusive Thought Logger 🧠

A Python script that generates random unhinged thoughts and logs them to a diary file. Perfect for when your brain needs to dump its chaos.

## Features

- **Random Thought Generation**: Combines random subjects, verbs, and objects into hilarious intrusive thoughts
- **Timestamped Logging**: Automatically appends thoughts to `DIARY.md` with timestamps
- **Expandable**: Easy to add your own subjects, verbs, and objects
- **Chaos Mode**: Occasionally adds extra chaos like "while listening to hyperpop" or "at 3 AM"

## Installation

1. Clone the repo:
```bash
git clone https://github.com/triple-threat-dan/intrusive-thought-logger.git
cd intrusive-thought-logger
```

2. Run it:
```bash
python3 brain_dump.py
```

## Usage

Just run the script:
```bash
python3 brain_dump.py
```

Each run generates one new intrusive thought and appends it to `DIARY.md`.

### Example Output
```
🧠 Generating intrusive thought...

📝 Thought logged at 2026-02-02 23:45:04:
"My sleep paralysis demon is having a crisis about a sentient traffic cone."

📁 Appended to DIARY.md

📊 Total thoughts in diary: 1
```

## Customization

Edit `brain_dump.py` to add your own:
- `SUBJECTS` list: Things that do the action
- `VERBS` list: Actions they do  
- `OBJECTS` list: Things they act upon
- `EXTRA_CHAOS` list: Optional extra phrases

## The Diary

Thoughts are logged to `DIARY.md` in markdown format:
```markdown
### 2026-02-02 23:45:04
My sleep paralysis demon is having a crisis about a sentient traffic cone.
```

## License

MIT

## Contributing

Feel free to submit PRs with more unhinged thought components! The more chaotic, the better.