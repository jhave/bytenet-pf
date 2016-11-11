config = {
	"decoder_filter_width": 3,
	"encoder_filter_width" : 3,
	"sample_size": 1000,
	"decoder_dilations": [1, 2, 4, 8, 16,
						  1, 2, 4, 8, 16,
						  1, 2, 4, 8, 16,
						  1, 2, 4, 8, 16,
						  1, 2, 4, 8, 16,
						  ],
	"residual_channels": 512,
	"n_target_quant": 256,
	"n_source_quant": 256,
}