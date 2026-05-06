How many activities are present in the whole workflow?	1
What is the final status of the workflow?	Completed
What is the time to completion of the workflow?	20h 00m 00s
List all the parameters of the first activity of the workflow	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What hardware was used in the workflow?	4x NVIDIA RTX 4090 (Consumer GPU Target)
Who is responsible for this workflow (person or username or entity)?	Empero AI
What was the specific execution order of the tasks?	qlora-adaptation
List all the parameters for the whole workflow process	batch: 64, len: 256k, precision: 4-bit, dropout: 0.05
What was the peak RAM consumption during the workflow?	
Has the model been trained in a distributed setting?	
What was the real-time power consumption (in Watts) of the GPU during the workflow?	
Which inputs influenced the output in the workflow?	base-weights, rl-dataset
What is the total energy use for completing the workflow?	
List all input files with size larger than 100Mb	
List all different file types used as input	Pretrained Hybrid Model (Mamba2/MoE/Attention), RL Training Mixture
Identify the largest output	openNemo-Cascade-2-30B-A3B
What is the science domain of the dataset?	
Does the dataset have a predetermined train-test split?	
How many samples are present in the whole dataset?	
What is the data type of the ground truth (if present)?	
What is the specific task for which the dataset was created?	
What is the size in byte of one sample?	
What is the total size of the whole dataset?	
What are the designed uses for this model?	Drop-in replacement weights for Nemotron-Cascade-2 using native PyTorch ops.
How many epochs have been used in the final training?	
How many model parameters (weights) does the model have?	30B total / 3B active parameters
What is the science domain of the model?	
What is the task solved by this model (regression or classification or forecast etc.)?	
What is the intended use of this model?	Drop-in replacement weights for Nemotron-Cascade-2 using native PyTorch ops.
What is the size of the final model in Mb?	
What technique was used to train the model?	4-bit Quantization & QLoRA Fine-tuning
What is the claimed performance of this model?	Training Loss: ~1.2 (final); Perplexity: Consistent with base model.
Are the performance shown in the pretrained version improved in the finetuning?	Loss parity with original NVIDIA training logs; successful 4-bit loading.