![icon](docs/_static/slim.png)

# SLiM: Structured Linear Maps

Drop in replacements for pytorch nn.Linear for stable learning and inductive priors 
in physics informed machine learning applications.

## [Complete documentation](https://pnnl.github.io/slim/)

## Install dependencies manually

```console
$ conda create -n slim python=3.7
$ conda install pytorch torchvision cudatoolkit=10.2 -c pytorch
$ pip install python-mnist
```

## Cite as

```yaml
@article{SLiM2022,
  title={{SLiM: Structured Linear Maps}},
  author={Tuor, Aaron and Drgona, Jan and Skomski, Mia},
  Url= {https://github.com/pnnl/neuromancer}, 
  year={2022}
}
```

## Related paper
```yaml
@inproceedings{NEURIPS2021_c9dd73f5,
 author = {Drgona, Jan and Mukherjee, Sayak and Zhang, Jiaxin and Liu, Frank and Halappanavar, Mahantesh},
 booktitle = {Advances in Neural Information Processing Systems},
 editor = {M. Ranzato and A. Beygelzimer and Y. Dauphin and P.S. Liang and J. Wortman Vaughan},
 pages = {24033--24047},
 publisher = {Curran Associates, Inc.},
 title = {On the Stochastic Stability of Deep Markov Models},
 url = {https://proceedings.neurips.cc/paper/2021/file/c9dd73f5cb96486f5e1e0680e841a550-Paper.pdf},
 volume = {34},
 year = {2021}
}
```