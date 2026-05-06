How many activities are present in the whole workflow?	answer not found
What is the final status of the workflow?	answer not found
What is the time to completion of the workflow?	answer not found
List all the parameters of the first activity of the workflow	answer not found
What hardware was used in the workflow?	GPU cluster, H100-80GB GPUs
Who is responsible for this workflow (person or username or entity)?	Meta Platforms Ireland Limited / Meta Platforms, Inc.
What was the specific execution order of the tasks?	answer not found
List all the parameters for the whole workflow process	answer not found
What was the peak RAM consumption during the workflow?	Peak RSS for 3B model: 7,419 MB (BF16 baseline), 4,060 MB (3B QLoRA)
Has the model been trained in a distributed setting?	answer not found
What was the real-time power consumption (in Watts) of the GPU during the workflow?	700 W
Which inputs influenced the output in the workflow?	Publicly available online data, up to 9T tokens; ai4privacy/pii-masking-200k dataset for finetuning
What is the total energy use for completing the workflow?	916,000 GPU hours; 240 tons CO2eq
List all input files with size larger than 100Mb	answer not found
List all different file types used as input	answer not found
Identify the largest output	answer not found
What is the science domain of the dataset?	Privacy, Natural Language Processing
Does the dataset have a predetermined train-test split?	Yes
How many samples are present in the whole dataset?	~209,000 examples
What is the data type of the ground truth (if present)?	Text (masked_text/target_text), privacy_mask (JSON), span_labels (array), mbert_bio_labels (array)
What is the specific task for which the dataset was created?	PII masking/redaction in text
What is the size in byte of one sample?	answer not found
What is the total size of the whole dataset?	answer not found
What are the designed uses for this model?	PII redaction in English text, placeholder mapping for downstream processing or audit
How many epochs have been used in the final training?	answer not found
How many model parameters (weights) does the model have?	3.21B
What is the science domain of the model?	Privacy, Natural Language Processing
What is the task solved by this model (regression or classification or forecast etc.)?	Text generation (PII redaction), token classification
What is the intended use of this model?	Commercial and research use for multilingual dialogue, agentic retrieval, summarization, PII redaction
What is the size of the final model in Mb?	3B QLoRA: 2,529 MB; 3B SpinQuant: 2,435 MB; 3B BF16: 6,129 MB
What technique was used to train the model?	Supervised fine-tuning (SFT), QLoRA (quantization + LoRA), Direct Preference Optimization (DPO)
What is the claimed performance of this model?	Exact match: ~0.67; Placeholder micro-F1: ~0.90 (P~0.91, R~0.90); Formatting errors: ~0.00
Are the performance shown in the pretrained version improved in the finetuning?	Yes, instruction-tuned models outperform base pretrained models on benchmarks