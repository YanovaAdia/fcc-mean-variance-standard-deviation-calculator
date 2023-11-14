import numpy as np


def calculate(list):

  if len(list) < 9 or len(list) > 9:
    raise ValueError("List must contain nine numbers.")
  ReshapedList = np.reshape(list, (3, 3))
  calculations = dict()
  calculations['mean'] = [
      np.mean(ReshapedList, axis=0).tolist(),
      np.mean(ReshapedList, axis=1).tolist(),
      np.mean(ReshapedList)
  ]
  calculations['variance'] = [
      np.var(ReshapedList, axis=0).tolist(),
      np.var(ReshapedList, axis=1).tolist(),
      np.var(ReshapedList)
  ]
  calculations['standard deviation'] = [
      np.std(ReshapedList, axis=0).tolist(),
      np.std(ReshapedList, axis=1).tolist(),
      np.std(ReshapedList)
  ]
  calculations['max'] = [
      np.max(ReshapedList, axis=0).tolist(),
      np.max(ReshapedList, axis=1).tolist(),
      np.max(ReshapedList)
  ]
  calculations['min'] = [
      np.min(ReshapedList, axis=0).tolist(),
      np.min(ReshapedList, axis=1).tolist(),
      np.min(ReshapedList)
  ]
  calculations['sum'] = [
      np.sum(ReshapedList, axis=0).tolist(),
      np.sum(ReshapedList, axis=1).tolist(),
      np.sum(ReshapedList)
  ]

  return calculations
