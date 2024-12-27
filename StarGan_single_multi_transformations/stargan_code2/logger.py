from tensorboardX import SummaryWriter

class Logger(object):
    """TensorBoard logger using tensorboardX."""
    
    def __init__(self, log_dir):
        """Initialize SummaryWriter."""
        self.writer = SummaryWriter(log_dir)

    def scalar_summary(self, tag, value, step):
        """Add scalar summary."""
        self.writer.add_scalar(tag, value, step)

# Usage example:
logger = Logger('logs')
logger.scalar_summary('accuracy', 0.95, 100)
