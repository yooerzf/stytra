.. Stytra documentation master file, created by
   sphinx-quickstart on Tue Apr 17 15:22:25 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. role:: small


Stytra
======
an open-source, integrated system for stimulation, tracking and closed-loop behavioral experiments
---------------------------------------------------------------------------------------------------

| Vilim Štih\ :sup:`#`\ , Luigi Petrucco\ :sup:`#`\ , Andreas M. Kist* and Ruben Portugues
| `Research Group of Sensorimotor Control <http://www.portugueslab.com>`_, `Max Planck Institute of Neurobiology <https://www.neuro.mpg.de/>`_, Martinsried, Germany

| :sup:`\#`\ :small:`These authors contributed equally to this work.`
| \*\ :small:`Current address: Department of Phoniatrics and Pediatric Audiology, University Hospital Erlangen, Medical School, Friedrich-Alexander-University Erlangen-Nürnberg, Germany.`

.. raw:: html

    <video width="100%" loop autoplay controls>

    <source src="<http://www.portugueslab.com/files/stytra_freeswim.webm"
            type="video/webm">

    <source src="http://www.portugueslab.com/files/stytra_freeswim.mp4"
            type="video/mp4">
    </video>



We present Stytra, a flexible, open-source software package, written in Python and
designed to cover all the general requirements involved in larval zebrafish behavioral
experiments. It provides :ref:`timed stimulus presentation<stim-desc>`, :ref:`interfacing with external devices<trig-desc>`
and simultaneous real-time :ref:`tracking <tracking-desc>` of behavioral parameters such as position,
orientation, tail and eye motion in both freely-swimming and head-restrained
preparations. Stytra logs all recorded quantities, metadata, and code version in
standardized formats to allow full provenance tracking, from data acquisition through
analysis to publication. The package is modular and expandable for different
experimental protocols and setups. Current releases can be found at
https://github.com/portugueslab/stytra. We also provide complete
documentation with examples for extending the package to new stimuli and hardware,
as well as a :ref:`schema and parts list <hardware-list>` for behavioral setups. We showcase Stytra by
:ref:`reproducing <reproduction>` previously published behavioral protocols in both head-restrained and
freely-swimming larvae. We also :ref:`demonstrate <imaging-example>` the use of the software in the context of a
calcium imaging experiment, where it interfaces with other acquisition devices. Our
aims are to enable more laboratories to easily implement behavioral experiments, as
well as to provide a platform for sharing stimulus protocols that permits easy
reproduction of experiments and straightforward validation. Finally, we demonstrate
how Stytra can serve as a platform to design behavioral experiments involving tracking
or visual stimulation with other animals and provide an `example integration <https://github.com/portugueslab/Stytra-with-DeepLabCut>`_ with the
DeepLabCut neural network-based tracking method.

If you are using Stytra for your own research, please `cite us <https://doi.org/10.1371/journal.pcbi.1006699>`_!

If you encounter any issues, please report them `here <https://github.com/portugueslab/stytra/issues>`_.


..  toctree::
    :maxdepth: 2
    :caption: Overview
    :glob:

    overview/*


..  toctree::
    :maxdepth: 2
    :caption: User guide
    :glob:

    userguide/*


..  toctree::
    :maxdepth: 2
    :caption: Developer guide
    :glob:

    devdocs/*