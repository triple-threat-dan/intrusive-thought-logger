#!/usr/bin/env python3
"""
Brain Dump AI - Enhanced Intrusive Thought Logger
Generates AI-augmented nested thoughts using Gemini CLI
"""

import random
import subprocess
from datetime import datetime
import os

# Collections of unhinged components
SUBJECTS = [
    "A raccoon",
    "My anxiety",
    "Elon Musk",
    "The ghost of Steve Jobs",
    "A sentient toaster",
    "My left sock",
    "The CIA",
    "A depressed cloud",
    "Shrek",
    "The concept of time",
    "A rogue AI",
    "My sleep paralysis demon",
    "A swarm of bees",
    "The IRS",
    "A philosophical potato",
    "My ex",
    "The illuminati",
    "A confused pigeon",
    "The last brain cell",
    "A haunted IKEA bookshelf"
]

VERBS = [
    "is eating",
    "yeeted",
    "ascended to",
    "is plotting against",
    "has fused with",
    "is questioning",
    "is aggressively hugging",
    "is flirting with",
    "is vibing with",
    "is dissociating into",
    "has become one with",
    "is conspiring with",
    "is aggressively knitting",
    "is doomscrolling through",
    "is having a crisis about",
    "is speedrunning",
    "is manifesting",
    "is gatekeeping",
    "is astral projecting into",
    "is having beef with"
]

OBJECTS = [
    "the sun",
    "a dumpster fire",
    "hot topic",
    "my existential dread",
    "a cursed fidget spinner",
    "the void",
    "my imposter syndrome",
    "a sentient traffic cone",
    "the algorithm",
    "my sleep schedule",
    "a haunted Kohl's cashier",
    "the patriarchy",
    "my credit score",
    "a philosophical quandary",
    "the backrooms",
    "my therapy bills",
    "a glitch in the matrix",
    "my student loans",
    "a conspiracy theory",
    "my emotional baggage"
]

def generate_base_thought():
    """Generate a base intrusive thought from our collections."""
    subject = random.choice(SUBJECTS)
    verb = random.choice(VERBS)
    obj = random.choice(OBJECTS)
    return f"{subject} {verb} {obj}."

def generate_ai_thought(base_thought=None):
    """Generate an AI-augmented nested thought using Gemini."""
    if base_thought is None:
        base_thought = generate_base_thought()
    
    # Craft a prompt for Gemini to expand the thought
    prompt = f"""
    Take this absurd thought: "{base_thought}"
    
    Transform it into a NESTED intrusive thought with this structure:
    "[SUBJECT] is [VERB] [OBJECT], which is [VERB2] [OBJECT2]."
    
    Make it surreal, absurd, and hilarious. Add metaphors, existential dread, or cosmic horror.
    Keep it concise - one sentence max. No markdown, just plain text.
    """
    
    try:
        result = subprocess.run(
            ["gemini", prompt.strip()],
            capture_output=True,
            text=True,
            timeout=30
        )
        
        if result.returncode == 0:
            ai_thought = result.stdout.strip()
            # Clean up any extra whitespace or quotes
            ai_thought = ai_thought.replace('"', '').replace("'", "").strip()
            return ai_thought
        else:
            print(f"Gemini error: {result.stderr}")
            return base_thought  # Fall back to base thought
    
    except subprocess.TimeoutExpired:
        print("Gemini timed out")
        return base_thought
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return base_thought

def generate_chain_thought(depth=2):
    """Generate a chain of nested thoughts."""
    current_thought = generate_base_thought()
    
    for i in range(depth - 1):
        # Use each iteration as inspiration for the next
        prompt = f"""
        Expand on this absurd thought: "{current_thought}"
        
        Add another layer of absurdity by connecting it to something else surreal.
        Use structure: "[...], and now [NEW_VERB] [NEW_OBJECT]."
        
        Keep it one sentence, weird, and hilarious.
        """
        
        try:
            result = subprocess.run(
                ["gemini", prompt.strip()],
                capture_output=True,
                text=True,
                timeout=30
            )
            
            if result.returncode == 0:
                current_thought = result.stdout.strip()
                current_thought = current_thought.replace('"', '').replace("'", "").strip()
        
        except:
            # If Gemini fails, just add a simple extension
            extra = random.choice(["while listening to hyperpop", "at 3 AM", "for clout", 
                                  "in a Walmart parking lot", "on main", "with malicious intent"])
            current_thought = f"{current_thought} {extra}"
    
    return current_thought

def log_thought(thought, mode="ai"):
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
    print("🧠🤖 Brain Dump AI - Enhanced Intrusive Thought Generator")
    print("=" * 50)
    
    print("\nChoose mode:")
    print("1. Classic (template-based)")
    print("2. AI Augmented (Gemini-enhanced)")
    print("3. Chain Reaction (nested thoughts)")
    
    try:
        choice = input("\nEnter choice (1-3, default 2): ").strip()
    except EOFError:
        choice = "2"
    
    if choice == "1":
        thought = generate_base_thought()
        mode = "classic"
    elif choice == "3":
        depth = input("Chain depth (2-4, default 3): ").strip()
        depth = int(depth) if depth.isdigit() and 2 <= int(depth) <= 4 else 3
        thought = generate_chain_thought(depth)
        mode = "chain"
    else:
        thought = generate_ai_thought()
        mode = "ai"
    
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