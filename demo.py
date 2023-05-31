from Insurance.pipeline.batch_prediction import start_batch_prediction
from Insurance.pipeline.training_pipeline import start_training_pipeline

if __name__=="__main__":
    try:
        
        output_file = start_training_pipeline()
        print(output_file)
    except Exception as e:
        print(e)