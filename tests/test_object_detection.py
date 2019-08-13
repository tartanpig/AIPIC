from imageai.Detection import ObjectDetection
import pytest
import os
import cv2
from os.path import dirname
import shutil
from numpy import ndarray

TEST_FOLDER = os.path.dirname(__file__)

image_input = os.path.join(TEST_FOLDER, "data-images", "11.jpg")
image_output = os.path.join(TEST_FOLDER, "data-temp", "11-detected.jpg")



@pytest.mark.detection
@pytest.mark.retinanet
def test_object_detection_retinanet():
    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    results = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40)

    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], ndarray)
    assert os.path.exists(image_output)
    os.remove(image_output)

    results2, extracted_paths  = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output,
                                              minimum_percentage_probability=40, extract_detected_objects=True)

    assert isinstance(results2, list)
    assert isinstance(extracted_paths, list)
    assert os.path.isdir(os.path.join(image_output + "-objects"))
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], ndarray)

    for extracted_path in extracted_paths:
        assert os.path.exists(extracted_path)

    shutil.rmtree(os.path.join(image_output + "-objects"))




@pytest.mark.detection
@pytest.mark.yolov3
def test_object_detection_yolov3():
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "yolo.h5"))
    detector.loadModel()
    results = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40)

    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], tuple)
    assert os.path.exists(image_output)
    os.remove(image_output)

    results2, extracted_paths = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output,
                                                                minimum_percentage_probability=40,
                                                                extract_detected_objects=True)

    assert isinstance(results2, list)
    assert isinstance(extracted_paths, list)
    assert os.path.isdir(os.path.join(image_output + "-objects"))
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], tuple)

    for extracted_path in extracted_paths:
        assert os.path.exists(extracted_path)

    shutil.rmtree(os.path.join(image_output + "-objects"))



@pytest.mark.detection
@pytest.mark.tiny_yolov3
def test_object_detection_tiny_yolov3():
    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "yolo-tiny.h5"))
    detector.loadModel()
    results = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40)

    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], tuple)
    assert os.path.exists(image_output)
    os.remove(image_output)

    results2, extracted_paths = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output,
                                                                minimum_percentage_probability=40,
                                                                extract_detected_objects=True)

    assert isinstance(results2, list)
    assert isinstance(extracted_paths, list)
    assert os.path.isdir(os.path.join(image_output + "-objects"))
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], tuple)

    for extracted_path in extracted_paths:
        assert os.path.exists(extracted_path)

    shutil.rmtree(os.path.join(image_output + "-objects"))






@pytest.mark.detection
@pytest.mark.retinanet
@pytest.mark.array_io
def test_object_detection_retinanet_array_io():

    image_input_array = cv2.imread(image_input)

    detector = ObjectDetection()
    detector.setModelTypeAsRetinaNet()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "resnet50_coco_best_v2.0.1.h5"))
    detector.loadModel()
    detected_array, results = detector.detectObjectsFromImage(input_image=image_input_array, input_type="array", minimum_percentage_probability=40, output_type="array")

    assert isinstance(detected_array, ndarray)
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], ndarray)

    detected_array, results2, extracted_arrays = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40, extract_detected_objects=True, output_type="array")

    assert isinstance(results2, list)
    assert isinstance(extracted_arrays, list)
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], ndarray)

    for extracted_array in extracted_arrays:
        assert isinstance(extracted_array, ndarray)




@pytest.mark.detection
@pytest.mark.yolov3
@pytest.mark.array_io
def test_object_detection_yolov3_array_io():

    image_input_array = cv2.imread(image_input)

    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "yolo.h5"))
    detector.loadModel()
    detected_array, results = detector.detectObjectsFromImage(input_image=image_input_array, input_type="array", minimum_percentage_probability=40, output_type="array")

    assert isinstance(detected_array, ndarray)
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], tuple)

    detected_array, results2, extracted_arrays = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40, extract_detected_objects=True, output_type="array")

    assert isinstance(results2, list)
    assert isinstance(extracted_arrays, list)
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], tuple)

    for extracted_array in extracted_arrays:
        assert isinstance(extracted_array, ndarray)


@pytest.mark.detection
@pytest.mark.tiny_yolov3
@pytest.mark.array_io
def test_object_detection_tiny_yolov3_array_io():

    image_input_array = cv2.imread(image_input)

    detector = ObjectDetection()
    detector.setModelTypeAsTinyYOLOv3()
    detector.setModelPath(os.path.join(TEST_FOLDER, "data-models", "yolo-tiny.h5"))
    detector.loadModel()
    detected_array, results = detector.detectObjectsFromImage(input_image=image_input_array, input_type="array", minimum_percentage_probability=40, output_type="array")

    assert isinstance(detected_array, ndarray)
    assert isinstance(results, list)
    for result in results:
        assert isinstance(result["name"], str)
        assert isinstance(result["percentage_probability"], float)
        assert isinstance(result["box_points"], tuple)

    detected_array, results2, extracted_arrays = detector.detectObjectsFromImage(input_image=image_input, output_image_path=image_output, minimum_percentage_probability=40, extract_detected_objects=True, output_type="array")

    assert isinstance(results2, list)
    assert isinstance(extracted_arrays, list)
    for result2 in results2:
        assert isinstance(result2["name"], str)
        assert isinstance(result2["percentage_probability"], float)
        assert isinstance(result2["box_points"], tuple)

    for extracted_array in extracted_arrays:
        assert isinstance(extracted_array, ndarray)