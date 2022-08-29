class Simtex < Formula
    include Language::Python::Virtualenv

    desc "Convert your markdown or text files into LaTeX/pdf with one command!"
    homepage "https://github.com/iaacornus/simtex"
    url "https://github.com/iaacornus/simtex/releases/download/v0.3.0-beta/simtex-0.3.0b0.tar.gz"
    sha256 "9513c0c778dc80d6d05e1b1560690d098aba0a61646d1d07efe112ba6b8fab45"
    license "GPL-3.0"

    def install
        virtualenv_install_with_resources
    end

    test do
        system "false"
    end
end
