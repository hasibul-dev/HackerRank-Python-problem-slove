class MultiHeadAttention(nn.Module):
    def __init__(self, d_model, num_heads):
        super().__init__()
        self.num_heads = num_heads
        self.d_model = d_model
        self.head_dim = d_model // num_heads
        self.query_linear = nn.Linear(d_model, d_model, bias=False)
        self.key_linear = nn.Linear(d_model, d_model, bias=False)
        self.value_linear = nn.Linear(d_model, d_model, bias=False)
        self.output_linear = nn.Linear(d_model, d_model)

    def split_heads(self, x, batch_size):
        seq_length = x.size(1)
        # Split the input embeddings and permute
        x = x.view(batch_size, seq_length, self.num_heads, self.head_dim)
        return x.permute(0, 2, 1, 3)
