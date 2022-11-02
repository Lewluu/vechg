
class Gesture:
    def setGesture(fingers):
        global _gesture
        _gesture = "NONE"

        # gesture iteration
        if fingers == ['pinky finger']:
            _gesture = "LEFT"
        if fingers == ['thumb']:
            _gesture = "RIGHT"
        if fingers == ['index finger']:
            _gesture = "FORWARD"
        if fingers == ['index finger', 'middle finger']:
            _gesture = "BACKWARD"
        if fingers == ['index finger', 'middle finger', 'ring finger']:
            _gesture = "JUMP"
        if fingers == ['index finger', 'pinky finger']:
            _gesture = "ROTATE LEFT"
        if fingers == ['index finger', 'thumb']:
            _gesture = "ROTATE RIGHT"
    
    def getGesture():
        return _gesture
    
