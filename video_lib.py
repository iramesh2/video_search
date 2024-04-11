# video_library.py
videos = {
    "video1": {
        "title": "How to Bake a Cake",
        "script": "Today, we're going to learn how to bake a simple cake. The ingredients you will need are..."
    },
    "video2": {
        "title": "Understanding the Basics of Python",
        "script": "Python is a high-level, interpreted, and general-purpose programming language. This video will cover the basics of Python..."
    },
    "video3": {
        "title": "The History of the Internet",
        "script": "The Internet started in the 1960s as a way for government researchers to share information. Computers in the '60s were large and immobile..."
    },
    "video4": {
        "title": "Basics of Gardening",
        "script": "Gardening can be a very rewarding hobby. In this video, we will cover the basics you need to know to start your own garden..."
    },
    "video5": {
        "title": "Introduction to Quantum Computing",
        "script": "Quantum computing is a rapidly growing technology that leverages the peculiarities of quantum mechanics to perform computations..."
    },
    "video6": {
        "title": "Meditation for Beginners",
        "script": "Meditation is a practice where an individual uses a technique – such as mindfulness, or focusing the mind on a particular object, thought..."
    },
    "video7": {
        "title": "The Art of Public Speaking",
        "script": "Public speaking is a valuable skill to have. This video will give you tips and techniques to captivate your audience from start to finish..."
    },
    "video8": {
        "title": "Introduction to Astrophysics",
        "script": "Astrophysics helps us understand the universe beyond our world. In this video, we'll introduce some basic concepts and marvels of the cosmos..."
    },
    "video9": {
        "title": "Yoga for Complete Beginners",
        "script": "Yoga is an ancient practice that can help improve your mental and physical health. This video is designed for complete beginners..."
    },
    "video10": {
        "title": "The Science of Nutrition",
        "script": "What you eat has a big impact on your health. In this video, we'll explore the science of nutrition and how your diet affects your body..."
    }
}
def print_video_titles():
    for video_id, video_info in videos.items():
        print(f"{video_id}: {video_info['title']}")