# import cv2
# import numpy as np
# import face_recognition
# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture 

# class FaceRecognitionApp(App):
#     def __init__(self, **kwargs):
#         super(FaceRecognitionApp, self).__init__(**kwargs)
#         self.video_capture = cv2.VideoCapture(0)
#         self.known_face_encodings = np.load("known_face_encodings.npy")
#         self.known_face_names = np.load("known_face_names.npy")
#         self.texture = None
#         self.face_names = []

#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         self.image = Image()
#         self.recognize_button = Button(text="Recognize")
#         self.recognize_button.bind(on_press=self.start_recognition)
#         self.recognized_faces_label = Label()
#         layout.add_widget(self.image)
#         layout.add_widget(self.recognize_button)
#         layout.add_widget(self.recognized_faces_label)
#         Clock.schedule_interval(self.update, 1.0 / 30.0)
#         return layout

#     def update(self, dt):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
#             self.image.texture = self.texture

#     def start_recognition(self, instance):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.face_locations = face_recognition.face_locations(frame)
#             face_encodings = face_recognition.face_encodings(frame, self.face_locations)
#             self.face_names = []

#             for face_encoding in face_encodings:
#                 matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#                 name = "Unknown"

#                 if True in matches:
#                     first_match_index = matches.index(True)
#                     name = self.known_face_names[first_match_index]

#                 self.face_names.append(name)

#             # Update the recognized faces label
#             self.recognized_faces_label.text = "Recognized faces: " + ", ".join(self.face_names)

# if __name__ == '__main__':
#     FaceRecognitionApp().run()





# import cv2
# import numpy as np
# import face_recognition
# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture

# class FaceRecognitionApp(App):
#     def __init__(self, **kwargs):
#         super(FaceRecognitionApp, self).__init__(**kwargs)
#         self.video_capture = cv2.VideoCapture(0)
#         self.known_face_encodings = np.load("known_face_encodings.npy")
#         self.known_face_names = np.load("known_face_names.npy")
#         self.texture = None
#         self.recognized_faces = []

#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         self.image = Image()
#         self.recognize_button = Button(text="Recognize")
#         self.recognize_button.bind(on_press=self.start_recognition)
#         self.recognized_faces_layout = ScrollView()
#         self.recognized_faces_grid = GridLayout(cols=1, size_hint_y=None)
#         self.recognized_faces_layout.add_widget(self.recognized_faces_grid)
#         layout.add_widget(self.image)
#         layout.add_widget(self.recognize_button)
#         layout.add_widget(self.recognized_faces_layout)
#         Clock.schedule_interval(self.update, 1.0 / 30.0)
#         return layout

#     def update(self, dt):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
#             self.image.texture = self.texture

#     def start_recognition(self, instance):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.face_locations = face_recognition.face_locations(frame)
#             face_encodings = face_recognition.face_encodings(frame, self.face_locations)
#             self.recognized_faces = []

#             for face_encoding in face_encodings:
#                 matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#                 name = "Unknown"

#                 if True in matches:
#                     first_match_index = matches.index(True)
#                     name = self.known_face_names[first_match_index]

#                 self.recognized_faces.append(name)

#             # Update the recognized faces label
#             self.update_recognized_faces()

#     def update_recognized_faces(self):
#         self.recognized_faces_grid.clear_widgets()
#         for name in self.recognized_faces:
#             label = Label(text=name)
#             self.recognized_faces_grid.add_widget(label)

# if __name__ == '__main__':
#     FaceRecognitionApp().run()

# import cv2
# import numpy as np
# import face_recognition
# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
# from datetime import datetime

# class FaceRecognitionApp(App):
#     def __init__(self, **kwargs):
#         super(FaceRecognitionApp, self).__init__(**kwargs)
#         self.video_capture = cv2.VideoCapture(0)
#         self.known_face_encodings = np.load("known_face_encodings.npy")
#         self.known_face_names = np.load("known_face_names.npy")
#         self.texture = None
#         self.recognized_faces = []

#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         self.image = Image()
#         self.recognize_button = Button(text="Recognize")
#         self.recognize_button.bind(on_press=self.start_recognition)
#         self.recognized_faces_layout = ScrollView()
#         self.recognized_faces_grid = GridLayout(cols=1, size_hint_y=None)
#         self.recognized_faces_layout.add_widget(self.recognized_faces_grid)
#         layout.add_widget(self.image)
#         layout.add_widget(self.recognize_button)
#         layout.add_widget(self.recognized_faces_layout)
#         Clock.schedule_interval(self.update, 1.0 / 30.0)
#         return layout

#     def update(self, dt):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
#             self.image.texture = self.texture

#     def start_recognition(self, instance):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.face_locations = face_recognition.face_locations(frame)
#             face_encodings = face_recognition.face_encodings(frame, self.face_locations)
#             self.recognized_faces = []

#             for face_encoding in face_encodings:
#                 matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#                 name = "Unknown"

#                 if True in matches:
#                     first_match_index = matches.index(True)
#                     name = self.known_face_names[first_match_index]

#                 timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#                 self.recognized_faces.append(f"{name} ({timestamp})")

#             # Update the recognized faces label
#             self.update_recognized_faces()

#     def update_recognized_faces(self):
#         self.recognized_faces_grid.clear_widgets()
#         for name in self.recognized_faces:
#             label = Label(text=name)
#             self.recognized_faces_grid.add_widget(label)

# if __name__ == '__main__':
#     FaceRecognitionApp().run()


# import cv2
# import numpy as np
# import face_recognition
# from kivy.app import App
# from kivy.uix.image import Image
# from kivy.uix.boxlayout import BoxLayout
# from kivy.uix.button import Button
# from kivy.uix.label import Label
# from kivy.uix.scrollview import ScrollView
# from kivy.uix.gridlayout import GridLayout
# from kivy.clock import Clock
# from kivy.graphics.texture import Texture
# from datetime import datetime

# class FaceRecognitionApp(App):
#     def __init__(self, **kwargs):
#         super(FaceRecognitionApp, self).__init__(**kwargs)
#         self.video_capture = cv2.VideoCapture(0)
#         self.known_face_encodings = np.load("known_face_encodings.npy")
#         self.known_face_names = np.load("known_face_names.npy")
#         self.texture = None
#         self.recognized_faces = []
#         self.recognizing = False

#     def build(self):
#         layout = BoxLayout(orientation='vertical')
#         self.image = Image()
#         self.recognize_button = Button(text="Recognize")
#         self.recognize_button.bind(on_press=self.toggle_recognition)
#         self.recognized_faces_layout = ScrollView()
#         self.recognized_faces_grid = GridLayout(cols=1, size_hint_y=None)
#         self.recognized_faces_layout.add_widget(self.recognized_faces_grid)
#         layout.add_widget(self.image)
#         layout.add_widget(self.recognize_button)
#         layout.add_widget(self.recognized_faces_layout)
#         Clock.schedule_interval(self.update, 1.0 / 30.0)
#         return layout

#     def update(self, dt):
#         ret, frame = self.video_capture.read()
#         if ret:
#             self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
#             self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
#             self.image.texture = self.texture

#         if self.recognizing:
#             self.recognize_faces(frame)

#     def toggle_recognition(self, instance):
#         self.recognizing = not self.recognizing

#     def recognize_faces(self, frame):
#         self.face_locations = face_recognition.face_locations(frame)
#         face_encodings = face_recognition.face_encodings(frame, self.face_locations)
#         self.recognized_faces = []

#         for face_encoding in face_encodings:
#             matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
#             name = "Unknown"

#             if True in matches:
#                 first_match_index = matches.index(True)
#                 name = self.known_face_names[first_match_index]

#             timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             self.recognized_faces.append(f"{name} ({timestamp})")

#         # Update the recognized faces label
#         self.update_recognized_faces()

#     def update_recognized_faces(self):
#         self.recognized_faces_grid.clear_widgets()
#         for name in self.recognized_faces:
#             label = Label(text=name)
#             self.recognized_faces_grid.add_widget(label)

# if __name__ == '__main__':
#     FaceRecognitionApp().run()



import cv2
import numpy as np
import face_recognition
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from datetime import datetime

class FaceRecognitionApp(App):
    def __init__(self, **kwargs):
        super(FaceRecognitionApp, self).__init__(**kwargs)
        self.video_capture = cv2.VideoCapture(0)
        self.known_face_encodings = np.load("known_face_encodings.npy")
        self.known_face_names = np.load("known_face_names.npy")
        self.texture = None
        self.recognized_faces = []

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.image = Image()
        self.recognize_button = Button(text="Recognize")
        self.recognize_button.bind(on_press=self.recognize_faces)
        self.recognized_faces_layout = ScrollView()
        self.recognized_faces_grid = GridLayout(cols=1, size_hint_y=None)
        self.recognized_faces_layout.add_widget(self.recognized_faces_grid)
        layout.add_widget(self.image)
        layout.add_widget(self.recognize_button)
        layout.add_widget(self.recognized_faces_layout)
        return layout

    def recognize_faces(self, instance):
        ret, frame = self.video_capture.read()
        if ret:
            self.texture = Texture.create(size=(frame.shape[1], frame.shape[0]), colorfmt='bgr')
            self.texture.blit_buffer(frame.tobytes(), colorfmt='bgr')
            self.image.texture = self.texture

        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = self.known_face_names[first_match_index]

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            self.recognized_faces.append(f"{name} ({timestamp})")

        self.update_recognized_faces()

    def update_recognized_faces(self):
        self.recognized_faces_grid.clear_widgets()
        for name in self.recognized_faces:
            label = Label(text=name)
            self.recognized_faces_grid.add_widget(label)

    def on_start(self):
        Clock.schedule_interval(self.recognize_faces, 1)  # Recognize every 1 second

if __name__ == '__main__':
    FaceRecognitionApp().run()
