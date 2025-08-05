### MongoDB Document Schema

**Collection:** `detections`

Each document contains:
- `filename`: `string` – name of the saved image
- `timestamp`: `datetime` – time when detection was made
- `detections`: `array[string]` – list of detected classes
- `image`: `binary` – image data in JPEG format
