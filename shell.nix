
{ pkgs ? import <nixpkgs> {} }:

let
  my-python-packages = ps: with ps; [
    jupyter
    ipynb
  ];

pkgs.mkShell {
  buildInputs = [
    pkgs.openjdk21
    pkgs.maven
    pkgs.git
  ];

  JAVA_HOME = "${pkgs.openjdk21}/lib/openjdk";
}