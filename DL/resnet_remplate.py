class ResNet:

  '''
  Reference codes below
  https://github.com/keras-team/keras-applications/blob/master/keras_applications/resnet50.py
  https://github.com/raghakot/keras-resnet

  arguments for each method are listed in below format
  ARGUMENT_NAME (DEFFAULT_VALUE)  : AVAILABLE_OPTIONS / DESCRIPTION_OF_ARGUMENT
  '''


  def __init__(self, **kwargs):
      '''
      selecting either of ResNet/ResNetV2/ResNext/SE-Resnet and controlling source model behaviour
      ------------------------------------
      include_top      (True)            : to include classification head on convolutional base
      num_classes      (10)              : number of output units in final softmax layer
      pooling          ('avg')           : global pooling to be applied after convolutional base base (None, 'avg', 'max')
      input_shape      ((None, None, 3)) : number of channels mandatory, integer shape required if using no pooling
      which            (50)              : 18,34 , 50,101,152
      bottleneck       (True)            : use bottleneck block (used in ResNet 50/101/152)
      width_multiplier (1)               : Wide-ResNet (number of convo channels multiplier)
      resnet_v2        (True)            : to place activation in residual or after addition
      senet            (True)            : to include Sequeeze-and-Excitation for convo channels
      resnext          (True)            : to divide convo part of residual into groups
      cardinality      (32)              : number of branches/groups to divide residual convo
      resnext_divisor  (16)              : divisor for channels to keep in each branch of ResNext block
      '''
      # Model config dictionary to be used by build() method to prepare final model
      self.model_config = { 
          18  : {}, 
          34  : {}, 
          50  : {}, 
          101 : {}, 
          152 : {}, 
          }
      self.__dict__.update()
  

  def build(self, activation='relu', **kwargs):
    '''
    model to build with given activation functions
    ---------------------
    activation ('relu') : hidden layer activation function (string OR layers.Activation instance)
    kwargs     ({})     : arguments to be passed to layers.Activation instance
    '''
    model = None
    return model