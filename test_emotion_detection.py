import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def check(self, text, expected):
        self.assertEqual(emotion_detector(text)['dominant_emotion'], expected)

    def test_emotions(self):
        self.check("I am glad this happened", "joy")
        self.check("I am really mad about this", "anger")
        self.check("I feel disgusted just hearing about this", "disgust")
        self.check("I am so sad about this", "sadness")
        self.check("I am really afraid that this will happen", "fear")


if __name__ == "__main__":
    unittest.main()
