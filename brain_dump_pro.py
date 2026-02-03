#!/usr/bin/env python3
"""
Brain Dump Pro - Dynamic Intrusive Thought Logger
Enhanced version with recursive/nested thoughts
"""

import random
from datetime import datetime
import os

# Expanded collections for more variety
SUBJECTS = [
    "A raccoon", "My anxiety", "Elon Musk", "The ghost of Steve Jobs", "A sentient toaster",
    "My left sock", "The CIA", "A depressed cloud", "Shrek", "The concept of time",
    "A rogue AI", "My sleep paralysis demon", "A swarm of bees", "The IRS", "A philosophical potato",
    "My ex", "The illuminati", "A confused pigeon", "The last brain cell", "A haunted IKEA bookshelf",
    "The algorithm's therapist", "A sentient USB cable", "My imposter syndrome", "A feral Roomba",
    "The ghost in the machine", "A melancholic algorithm", "My inner child", "A possessed Alexa",
    "The WiFi signal", "A glitch in reality"
]

VERBS = [
    "is eating", "yeeted", "ascended to", "is plotting against", "has fused with",
    "is questioning", "is aggressively hugging", "is flirting with", "is vibing with",
    "is dissociating into", "has become one with", "is conspiring with", "is aggressively knitting",
    "is doomscrolling through", "is having a crisis about", "is speedrunning", "is manifesting",
    "is gatekeeping", "is astral projecting into", "is having beef with",
    "is therapy-shopping with", "is trauma-bonding with", "is gaslighting", "is shadow-working",
    "is doom-buying", "is rage-quitting", "is maladaptive daydreaming about", "is catastrophizing with",
    "is dissociating from", "is hyperfixating on"
]

OBJECTS = [
    "the sun", "a dumpster fire", "hot topic", "my existential dread", "a cursed fidget spinner",
    "the void", "my imposter syndrome", "a sentient traffic cone", "the algorithm", "my sleep schedule",
    "a haunted Kohl's cashier", "the patriarchy", "my credit score", "a philosophical quandary",
    "the backrooms", "my therapy bills", "a glitch in the matrix", "my student loans",
    "a conspiracy theory", "my emotional baggage",
    "the collective unconscious", "a TikTok trend", "the simulation", "my parasocial relationships",
    "the cognitive dissonance", "a liminal space", "my attachment style", "the capitalist hellscape",
    "the dopamine hit", "my unresolved trauma"
]

CHAOS_PHRASES = [
    "while listening to hyperpop", "at 3 AM", "for clout", "in a Walmart parking lot", "on main",
    "with malicious intent", "during Mercury retrograde", "for the aesthetic", "to avoid taxes",
    "as a cry for help", "to feel something", "to avoid my responsibilities", "to impress my sleep paralysis demon",
    "in the backrooms", "for character development", "as a coping mechanism", "to assert dominance",
    "to avoid eye contact with God", "as an elaborate bit", "to farm engagement"
]

def generate_thought(depth=1):
    """Generate a random intrusive thought with optional nesting."""
    if depth <= 1:
        # Base case: simple thought
        subject = random.choice(SUBJECTS)
        verb = random.choice(VERBS)
        obj = random.choice(OBJECTS)
        
        if random.random() < 0.4:
            extra = random.choice(CHAOS_PHRASES)
            return f"{subject} {verb} {obj} {extra}."
        else:
            return f"{subject} {verb} {obj}."
    else:
        # Recursive case: nested thought
        connector = random.choice([
            ", which is", ", and now", ", meanwhile", ", which has started",
            ", but secretly", ", while also", ", and suddenly", ", which triggered"
        ])
        
        first_part = generate_thought(depth=1)
        second_part = generate_thought(depth=depth-1).lower()
        
        # Remove the period from first part if present
        first_part = first_part.rstrip('.')
        
        # Capitalize the second part appropriately
        second_part_words = second_part.split()
        if second_part_words:
            second_part_words[0] = second_part_words[0].capitalize()
            second_part = ' '.join(second_part_words)
        
        return f"{first_part}{connector} {second_part}"

def generate_story(num_thoughts=3):
    """Generate a chain of related thoughts forming a mini-story."""
    theme = random.choice([
        "existential dread", "late capitalism", "internet culture", "mental health",
        "the simulation", "ghosts", "technology", "social media", "therapy"
    ])
    
    characters = random.sample(SUBJECTS, 2)
    
    story = []
    for i in range(num_thoughts):
        if i == 0:
            thought = f"{characters[0]} {random.choice(VERBS)} {random.choice(OBJECTS)} related to {theme}."
        elif i == num_thoughts - 1:
            thought = f"Meanwhile, {characters[1]} {random.choice(VERBS)} {random.choice(OBJECTS)}, creating a feedback loop of {theme}."
        else:
            connector = random.choice(["This caused", "Which led to", "As a result", "Somehow"])
            thought = f"{connector} {random.choice(SUBJECTS)} {random.choice(VERBS)} {random.choice(OBJECTS)}."
        
        if random.random() < 0.3:
            thought = thought.rstrip('.') + f" {random.choice(CHAOS_PHRASES)}."
        
        story.append(thought)
    
    return " ".join(story)

def log_thought(thought, mode="dynamic"):
    """Log the thought to DIARY.md with timestamp."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"### {timestamp} [{mode.upper()}]\n{thought}\n\n"
    
    # Create DIARY.md if it doesn't exist
    if not os.path.exists("DIARY.md"):
        with open("DIARY.md", "w") as f:
            f.write("# Intrusive Thought Diary\n\n*Unhinged thoughts generated by brain_dump.py*\n\n---\n\n")
    
    # Append the new thought
    with open("DIARY.md", "a") as f:
        f.write(log_entry)
    
    return timestamp

def main():
    """Main function to generate and log thoughts."""
    print("🧠 Brain Dump Pro - Dynamic Intrusive Thought Generator")
    print("=" * 50)
    
    print("\nChoose mode:")
    print("1. Simple (single thought)")
    print("2. Nested (recursive thoughts, depth 2-4)")
    print("3. Story Mode (connected thoughts)")
    
    try:
        choice = input("\nEnter choice (1-3, default 1): ").strip()
    except EOFError:
        choice = "1"
    
    if choice == "2":
        depth = input("Nesting depth (2-4, default 3): ").strip()
        depth = int(depth) if depth.isdigit() and 2 <= int(depth) <= 4 else 3
        thought = generate_thought(depth)
        mode = "nested"
    elif choice == "3":
        num = input("Number of thoughts in story (2-5, default 3): ").strip()
        num = int(num) if num.isdigit() and 2 <= int(num) <= 5 else 3
        thought = generate_story(num)
        mode = "story"
    else:
        thought = generate_thought(1)
        mode = "simple"
    
    timestamp = log_thought(thought, mode)
    
    print(f"\n📝 Thought generated ({mode}):")
    print(f"\"{thought}\"")
    print(f"\n⏰ Logged at {timestamp}")
    print(f"📁 Appended to DIARY.md")
    
    # Show DIARY.md stats
    if os.path.exists("DIARY.md"):
        with open("DIARY.md", "r") as f:
            content = f.read()
            thought_count = content.count("###")
            print(f"\n📊 Total thoughts in diary: {thought_count}")

if __name__ == "__main__":
    main()