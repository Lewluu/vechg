
class Gesture:
    def setGesture(fingers):
        global _gesture
        _gesture = "NONE"

        if fingers == ['pinky finger']:
            _gesture = "LEFT"
    
    def getGesture():
        return _gesture
    
