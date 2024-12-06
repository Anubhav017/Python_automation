import os

import allure
import pytest

from locator.locators import ScriptToVideoLocators, HomeLocators, MyProjectLocators, EditVideoLocators, \
    ArticleToVideoLocators, PPTtoVideoLocators
from pageObjects.pictryPages.ArticleVideoGenerate import ArticleToVideo
from pageObjects.pictryPages.LogInPage import LogInPage
from pageObjects.pictryPages.MemoryusagePage import MemoryUsage
from pageObjects.pictryPages.ScriptToVideo import ScriptToVideo
from pageObjects.pictryPages.editvideoGenerate import EditvideoGenerate
from pageObjects.pictryPages.memoryLeak import MemoryLeak
from pageObjects.pictryPages.scriptvideoGenerate import scriptvideoGenerate
from playwrighttests.conftest import logger, playwright_context_and_page
from testData.TestDataScript.test_data_Project import TestDataForProject


@allure.feature("Script To Video Feature")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.usefixtures("config")
class TestVideoGenerate:
    script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 0)
    article_email, article_password = TestDataForProject.get_login_credential("ArticleToVideo", 0)
    edit_email, edit_password = TestDataForProject.get_login_credential("EditVideo", 0)
    visual_email, visual_password = TestDataForProject.get_login_credential("VisualToVideo", 0)

    @allure.title("Download video from Script to video generate test")
    @allure.description("Video generate --> Download video from Script to video generate")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.VideoGen
    def test_script_to_video_generate(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            name = "ScriptToVideo" + ScriptToVideo.random_generator()
            memoryLeak.login_pictoryapp(self.script_email, self.script_password)

            logger.info("Clicking on Proceed button")
            videoGen.dynamicbar_invisible_scrolClick(ScriptToVideoLocators.Proceed_buton[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

        with allure.step("Navigating to the script Page"):
            logger.info("Navigating to the script Page")
            toggle_buttons, clip_Board, font_weight = videoGen.get_script_editor_highlight_page(name)

            assert font_weight in ["700", "bold"], "The text is not bold"
            assert clip_Board.is_enabled(), "clipBoard button is not enabled"

            for toggle_button in toggle_buttons:
                assert toggle_button.is_enabled(), "Not all toggle buttons are enabled"

            logger.info("Navigating from script Page to Storyboard Page")
            if videoGen.get_Storyboard_Page_scriptDownload(ScriptToVideoLocators.saved[1]):
                logger.info("Applying brand on the video")
                element = videoGen.get_apply_brand(ScriptToVideoLocators.branding[1])
                if element:
                    assert element.text_content() == "brand applied successfully", f"Expected 'brand applied successfully', but got '{element.text_content()}'"

                with allure.step("Apply Voiceover -->> Standard"):
                    logger.info("Applying voiceOver on the video")
                    voice_applied = videoGen.get_status_voiceover(ScriptToVideoLocators.Audio[1])
                    assert voice_applied.text_content() == "Applied"

                    videoGen.do_click(ScriptToVideoLocators.WaterMarks[1])

                with allure.step("Apply layer -->> copyScene"):
                    logger.info("Applying layer -->> copyScene")
                    copyScene = videoGen.get_apply_layer_visual(ScriptToVideoLocators.Visual[1])
                    assert copyScene is not None, "Button not found on the page"
                    videoGen.get_delete_layer_visual(ScriptToVideoLocators.DeleteLayer[1])

                with allure.step("Get the final memory usage"):
                    final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                with allure.step("Check for memory leaks"):
                    memory_difference_mb = final_memory_usage - initial_memory_usage
                    MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

                    print(f"{memory_difference_mb:.2f}:mb")
                    assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                with allure.step("Navigate to the story Page"):
                    logger.info("Navigate to the story Page")
                    story_scene = videoGen.get_story_scene(ScriptToVideoLocators.scene1[1])
                    if story_scene:
                        assert story_scene.text_content() == "Scene 1"

                with allure.step("Apply transition the scene"):
                    logger.info("Apply transition the scene")
                    videoGen.get_transition_scene(ScriptToVideoLocators.transition[1])

                with allure.step("Navigate to the element Page"):
                    logger.info("Navigate to the element Page")
                    element_apply = videoGen.get_Element_apply(ScriptToVideoLocators.element_apply[1])
                    if element_apply:
                        assert element_apply.text_content() == "Element copied to all scenes.", f"Expected 'Element copied to all scenes', but got '{element.text_content()}'"

                    with allure.step("Navigate to the format Page"):
                        logger.info("Navigate to the format Page")
                        porTrait = videoGen.get_Format_apply(ScriptToVideoLocators.format[1])
                        if porTrait:
                            assert porTrait is not None, "Button not found on the page"

                        with allure.step("Navigate to My Project Page"):
                            logger.info("Navigating to My Project Page")
                            Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    print(video_generation_text)
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"
                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

                            videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                        with allure.step("Check video element is present on Page"):
                            videoGen.is_videoscript_visible(name)

                        with allure.step("Check video URL is present on Page"):
                            element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                            if element:
                                video = videoGen.is_url_exist_myvideos()
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("Download video from Script to video French generate test")
    @allure.description("Video generate --> Download video from Script to video French generate")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.VideoGen
    def test_script_to_video_generate_French(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 8)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            name = "ScriptenVido" + ScriptToVideo.random_generator()
            memoryLeak.login_pictoryapp(script_email, script_password)

            logger.info("Clicking on Proceed button")
            videoGen.dynamicbar_invisible_scrolClick(ScriptToVideoLocators.Proceed_buton[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

        with allure.step("Navigating to the script Page"):
            logger.info("Navigating to the script Page")
            toggle_buttons, clip_Board, font_weight = videoGen.get_script_editor_french_highlight_page(name)

            assert font_weight in ["700", "bold"], "The text is not bold"
            assert clip_Board.is_enabled(), "clipBoard button is not enabled"

            for toggle_button in toggle_buttons:
                assert toggle_button.is_enabled(), "Not all toggle buttons are enabled"

            logger.info("Navigating from script Page to Storyboard Page")
            if videoGen.get_Storyboard_Page_scriptDownload(ScriptToVideoLocators.saved[1]):
                logger.info("Applying brand on the video")
                element = videoGen.get_apply_brand(ScriptToVideoLocators.branding[1])
                if element:
                    assert element.text_content() == "brand applied successfully", f"Expected 'brand applied successfully', but got '{element.text_content()}'"

                with allure.step("Apply Voiceover -->> Standard"):
                    logger.info("Applying voiceOver on the video")
                    voice_applied = videoGen.get_status_voiceover_multilang(ScriptToVideoLocators.Audio[1])
                    assert voice_applied.text_content() == "Applied"

                    videoGen.do_click(ScriptToVideoLocators.WaterMarks[1])

                with allure.step("Get the final memory usage"):
                    final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                with allure.step("Check for memory leaks"):
                    memory_difference_mb = final_memory_usage - initial_memory_usage
                    MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

                    print(f"{memory_difference_mb:.2f}:mb")
                    assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                    with allure.step("Navigate to the format Page"):
                        logger.info("Navigate to the format Page")
                        porTrait = videoGen.get_Format_apply(ScriptToVideoLocators.format[1])
                        if porTrait:
                            assert porTrait is not None, "Button not found on the page"

                        with allure.step("Navigate to My Project Page"):
                            logger.info("Navigating to My Project Page")
                            Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    print(video_generation_text)
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"
                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

                            videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                        with allure.step("Check video element is present on Page"):
                            videoGen.is_videoscript_visible(name)

                        with allure.step("Check video URL is present on Page"):
                            element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                            if element:
                                video = videoGen.is_url_exist_myvideos()
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("Edit to video generate with upload video test")
    @allure.description("Edit to Video generate --> Edit to video with upload video test")
    @allure.title("Edit to video generate with youtube Url test")
    @allure.description("Edit to Video generate --> Edit to video with youtube Url test")
    @pytest.mark.VideoGen
    def test_Edit_video_generate(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)
        EditvideoGen = EditvideoGenerate(page)

        with allure.step("Login to Pictory"):
            logger.info("Logging into Pictory")

            memoryLeak.login_pictoryapp(self.edit_email, self.edit_password)
            EditvideoGen.background_click(EditVideoLocators.Proceed_buton[1])

            # youtube_url = "https://www.youtube.com/watch?v=GTL4zhtEElI"
            # EditvideoGen.editPage_URL(youtube_url)
            # videoGen.scrollToclick_element(EditVideoLocators.Proceed_video[1])

            # videoGen.click_apply_button(EditVideoLocators.demo_vid[1])

            EditvideoGen.get_uploadmp4_file("input[type='file']", os.path.join('videoGen', 'evut.mp4'))
            EditvideoGen.get_Proceed_buton_click()

        with allure.step("Navigate to Summary Page and check element"):
            logger.info("Navigate to Summary Page and check element")
            transcription = EditvideoGen.do_element(f"#{EditVideoLocators.Transcription[1]}")
            assert transcription.is_visible(), f"Element with name '{transcription.text_content()}' is not present on the page."
            print(transcription.text_content())

            attribute = EditvideoGen.Attribute_name()
            if attribute:
                name = attribute.get_attribute("value")
            else:
                logger.error("Failed to retrieve the attribute name.")
                assert False, "Attribute name not found."

            logger.info("On Summary Page - > check highlight")
            highlight = EditvideoGen.do_element(f"#{EditVideoLocators.highlight[1]}")
            assert highlight.is_enabled(), f"Element with name '{highlight.text_content()}' is not enabled on the page."
            print(highlight.text_content())

        with allure.step("Navigate to edit video Page and check default brand selected"):
            default_brand = EditvideoGen.do_element(EditVideoLocators.defaultbrand[1])
            assert default_brand.text_content() == "brand01", f"Expected brand to be 'brand01', but found {default_brand.text_content()}"
            print(default_brand.text_content())

            brand_initial_memory_usage = MemoryUsage.log_memory_usage("Initial ")

            customize_video = EditvideoGen.do_element(EditVideoLocators.CustomizeVideo[1])
            assert customize_video.is_enabled(), f"Element with name '{customize_video.text_content()}' is not enabled on the page."
            print(customize_video.text_content())

            EditvideoGen.scrollToclick_element(EditVideoLocators.CustomizeVideo[1])

            logger.info("Applying brand on the video")
            branding = EditvideoGen.get_apply_brand(ScriptToVideoLocators.branding[1])
            assert branding.text_content() == "brand applied successfully", f"Expected 'brand applied successfully', but got '{branding.text_content()}'"

            brand_final_memory_usage = MemoryUsage.log_memory_usage("Final")

        with allure.step("Check for memory leaks"):
            memory_difference_mb = brand_final_memory_usage - brand_initial_memory_usage
            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

            print(f"{memory_difference_mb:.2f}:mb")
            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {brand_initial_memory_usage:.2f} MB, Final: {brand_final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

        with allure.step("Get the initial memory usage"):
            audio_initial_memory_usage = MemoryUsage.log_memory_usage("Initial ")

        with allure.step("Navigate to the desired tab"):
            memoryLeak.get_StoryboardPage_audio()

        with allure.step("Wait for and interact with elements"):
            memoryLeak.get_Vo_BGM_page()

        with allure.step("Get the final memory usage"):
            audio_final_memory_usage = MemoryUsage.log_memory_usage("Final ")

        with allure.step("Check for memory leaks"):
            memory_difference_mb = audio_final_memory_usage - audio_initial_memory_usage
            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)
            print(f"{memory_difference_mb:.2f}:mb")
            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {audio_initial_memory_usage:.2f} MB, Final: {audio_final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

        with allure.step("Navigate to My Project Page"):
            logger.info("Navigating to My Project Page")
            Video_Generation = EditvideoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
            if Video_Generation:
                video_generation_text = Video_Generation.text_content()
                if "Video Generation is completed" in video_generation_text:
                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                    print(video_generation_text)

                elif "Video Generation Failed" in video_generation_text:
                    print(video_generation_text)
                    assert False, "Video Generation Failed"

                elif "Video generation errored." in video_generation_text:
                    print(video_generation_text)
                    assert False, "Video generation errored"

                videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                with allure.step("Check video element is present on Page"):
                    if videoGen.is_videoscript_visible(name):
                        element = videoGen.dynamicbar_invisible(MyProjectLocators.Myproject_loader[1])
                        if element:
                            video = videoGen.is_url_exist_myvideos()
                            if video:
                                video_src = video.get_attribute("src")
                                assert video_src, "Video src attribute is empty."
                                print("Video URL:", video_src)

    @allure.title("Blog to video generate with youtube Url test")
    @allure.description("Blog to Video generate --> Blog to video with youtube Url test")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_BlogTo_video_generate(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)
        articlevideoGen = ArticleToVideo(page)

        with allure.step("Step 1: Login to Pictory"):
            # name = "ArticleToVideo" + ArticleToVideo.random_generator()
            memoryLeak.login_pictoryapp(self.article_email, self.article_password)

        with allure.step("Step 2: Generate ArticleTo Video"):
            logger.info("Generating article to video.")
            articlevideoGen.scrollToclick_element(ArticleToVideoLocators.Proceed_buton[1])

            articlevideoGen.Atricle_URL()
            articlevideoGen.scrollToclick_element(f"#{ArticleToVideoLocators.generate_vid[1]}")

            article = articlevideoGen.do_element(ArticleToVideoLocators.source[1])
            if article:
                logger.info("Article element found.")
                attribute = articlevideoGen.Attribute_name()
                if attribute:
                    name = attribute.get_attribute("value")
                else:
                    logger.error("Failed to retrieve the attribute name.")
                    assert False, "element no found"

                logger.info("Attribute name value: %s", name)
                nextButn = videoGen.do_element(ArticleToVideoLocators.next[1])
                if nextButn:
                    articlevideoGen.background_click(ArticleToVideoLocators.next[1])
                    logger.info("Proceed button clicked and all toggle buttons are enabled.")

                with allure.step("Get the initial memory usage"):
                    audio_initial_memory_usage = MemoryUsage.log_memory_usage("Initial ")

                with allure.step("Apply Voiceover -->> Premium"):
                    voice_applied = articlevideoGen.get_status_voiceover(ScriptToVideoLocators.Audio[1])
                    assert voice_applied.text_content() == "Applied"
                    logger.info("Voiceover applied successfully.")

                    with allure.step("Get the final memory usage"):
                        audio_final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                    with allure.step("Check for memory leaks"):
                        memory_difference_mb = audio_final_memory_usage - audio_initial_memory_usage
                        allure.attach(f"{memory_difference_mb:.2f}:MB", name="Memory Usage Difference (MB)", attachment_type=allure.attachment_type.TEXT)
                        assert memory_difference_mb < 500, f"Memory leak detected! Initial: {audio_initial_memory_usage}, Final: {audio_final_memory_usage}, Difference: {memory_difference_mb}"

                        with allure.step("Navigate to Video Generation Completed Page"):
                            Video_Generation = articlevideoGen.get_Video_Generation_Completed_Article(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                    print(video_generation_text)

                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"

                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

                            videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                        with allure.step("Check video element is present on Page"):
                            if articlevideoGen.is_videoscript_visible(name):
                                element = videoGen.dynamicbar_invisible(MyProjectLocators.Myproject_loader[1])
                                if element:
                                    img = articlevideoGen.is_url_exist_myimage()
                                    if img:
                                        img_src = img.get_attribute("src")
                                        assert img_src, f"Video src attribute for '{img_src}' is empty."
                                        print("Video URL:", img_src)

    @allure.title("Edit to video generate with upload video -->Download video clip")
    @allure.description("Edit to Video generate --> Edit to video with upload video test -->Download video clip")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_Edit_video_generate_Download_video_clip(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        EditvideoGen = EditvideoGenerate(page)

        edit_email, edit_password = TestDataForProject.get_login_credential("EditVideo", 3)

        with allure.step("Login to Pictory"):
            logger.info("Logging into Pictory")

            memoryLeak.login_pictoryapp(edit_email, edit_password)
            EditvideoGen.background_click(EditVideoLocators.Proceed_buton[1])

            EditvideoGen.get_uploadmp4_file("input[type='file']", os.path.join('videoGen', 'evut.mp4'))
            EditvideoGen.get_Proceed_buton_click()

            initial_memory_usage = MemoryUsage.log_memory_usage("Initial ")

        with allure.step("Navigate to Summary Page and check element"):
            logger.info("Navigate to Summary Page and check element")
            transcription = EditvideoGen.do_element(f"#{EditVideoLocators.Transcription[1]}")
            assert transcription.is_visible(), f"Element with name '{transcription.text_content()}' is not present on the page."
            print(transcription.text_content())

            logger.info("On Summary Page - > check highlight")
            highlight = EditvideoGen.do_element(f"#{EditVideoLocators.highlight[1]}")
            if highlight:
                assert highlight.is_enabled(), f"Element with name '{highlight.text_content()}' is not enabled on the page."
                print(highlight.text_content())

            with allure.step("Navigate to edit video Page and check default brand selected"):
                default_brand = EditvideoGen.do_element(EditVideoLocators.defaultbrand[1])
                assert default_brand.text_content() == "brand01", f"Expected brand to be 'brand01', but found {default_brand.text_content()}"
                print(default_brand.text_content())

                customize_video = EditvideoGen.do_element(EditVideoLocators.CustomizeVideo[1])
                assert customize_video.is_enabled(), f"Element with name '{customize_video.text_content()}' is not enabled on the page."
                print(customize_video.text_content())

                playvid = EditvideoGen.do_element(EditVideoLocators.playvid[1])
                if playvid:
                    EditvideoGen.scrollToclick_element(EditVideoLocators.playvid[1])
                    pausevid = EditvideoGen.do_element(EditVideoLocators.pausevid[1])
                    if pausevid:
                        assert (pausevid.is_enabled(),
                                f"element with name '{pausevid.text_content()}' is not present on the page.")
                        print(pausevid.text_content())

                    highlight = EditvideoGen.do_element(f"#{EditVideoLocators.highlight[1]}")
                    if highlight:
                        assert (highlight.is_enabled(), f"element with name '{highlight.text_content()}' is not present on the page.")
                        print(highlight.text_content())

                    with allure.step("Get the final memory usage"):
                        final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                    with allure.step("Check for memory leaks"):
                        memory_difference_mb = final_memory_usage - initial_memory_usage
                        MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)
                        print(f"{memory_difference_mb:.2f}:mb")
                        assert memory_difference_mb < 500, f"Memory leak detected! Initial: {initial_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                    with allure.step("Download video clip from storyboard Page"):
                        video_clip = EditvideoGen.editPage_summaryclip_video(EditVideoLocators.TranscriptionText[1])
                        if video_clip:
                            EditvideoGen.scrollToclick_element(EditVideoLocators.video_clip[1])

                            Video_Generation_Progress = EditvideoGen.get_Video_Generation_element(ScriptToVideoLocators.Video_Generation_Progress[1])
                            if Video_Generation_Progress:
                                assert Video_Generation_Progress.text_content() == "Video generation is in progress"
                                print(Video_Generation_Progress.text_content())

                            with allure.step("Navigate to My Video Generation"):
                                logger.info("Navigating to My Video Generation")
                                Video_Generation = EditvideoGen.get_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                                if Video_Generation:
                                    video_generation_text = Video_Generation.text_content()
                                    if "Video Generation is completed" in video_generation_text:
                                        assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                        print(video_generation_text)

                                    elif "Video Generation Failed" in video_generation_text:
                                        print(video_generation_text)
                                        assert False, "Video Generation Failed"

                                    elif "Video generation errored." in video_generation_text:
                                        print(video_generation_text)
                                        assert False, "Video generation errored"

    @allure.title("Edit to video generate with upload video -->Download highlight video")
    @allure.description("Edit to Video generate --> Edit to video with upload video -->Download highlight video ")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_Edit_video_generate_Download_highlight_video(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        EditvideoGen = EditvideoGenerate(page)

        edit_email, edit_password = TestDataForProject.get_login_credential("EditVideo", 3)

        with allure.step("Login to Pictory"):
            logger.info("Logging into Pictory")

            memoryLeak.login_pictoryapp(edit_email, edit_password)
            EditvideoGen.background_click(EditVideoLocators.Proceed_buton[1])

            EditvideoGen.get_uploadmp4_file("input[type='file']", os.path.join('videoGen', 'evut.mp4'))
            EditvideoGen.get_Proceed_buton_click()

            initial_memory_usage = MemoryUsage.log_memory_usage("Initial ")

        with allure.step("Navigate to Summary Page and check element"):
            logger.info("Navigate to Summary Page and check element")
            transcription = EditvideoGen.do_element(f"#{EditVideoLocators.Transcription[1]}")
            assert transcription.is_visible(), f"Element with name '{transcription.text_content()}' is not present on the page."
            print(transcription.text_content())

            logger.info("On Summary Page - > check highlight")
            highlight = EditvideoGen.do_element(f"#{EditVideoLocators.highlight[1]}")
            if highlight:
                assert highlight.is_enabled(), f"Element with name '{highlight.text_content()}' is not enabled on the page."
                print(highlight.text_content())

            with allure.step("Navigate to edit video Page and check default brand selected"):
                logger.info("Navigate to edit video Page and check default brand selected")
                default_brand = EditvideoGen.do_element(EditVideoLocators.defaultbrand[1])
                assert default_brand.text_content() == "brand01", f"Expected brand to be 'brand01', but found {default_brand.text_content()}"
                print(default_brand.text_content())

                customize_video = EditvideoGen.do_element(EditVideoLocators.CustomizeVideo[1])
                assert customize_video.is_enabled(), f"Element with name '{customize_video.text_content()}' is not enabled on the page."
                print(customize_video.text_content())

            with allure.step("Navigate to edit video Page and check Auto highlight enable"):
                logger.info("Navigate to edit video Page and check Auto highlight enable")
                autohighlight = EditvideoGen.get_summary_autohighlight_element(EditVideoLocators.autohighlight[1])
                if autohighlight:
                    assert autohighlight.text_content() == "Auto highlight"
                    print(autohighlight.text_content())

                else:

                    print("Auto highlight element not found .")
                    assert False, "Auto highlight element not found."

                with allure.step("Get the final memory usage"):
                    final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                with allure.step("Check for memory leaks"):
                    memory_difference_mb = final_memory_usage - initial_memory_usage
                    MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)
                    print(f"{memory_difference_mb:.2f}:mb")
                    assert memory_difference_mb < 500, f"Memory leak detected! Initial: {initial_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                with allure.step("Download video clip from storyboard Page"):
                    highlightvideo = EditvideoGen.editPage_summary_highlightVideo(EditVideoLocators.TranscriptionText[1])
                    if highlightvideo:
                        # EditvideoGen.scrollToclick_element(EditVideoLocators.video_clip[1])

                        Video_Generation_Progress = EditvideoGen.get_Video_Generation_element(ScriptToVideoLocators.Video_Generation_Progress[1])
                        if Video_Generation_Progress:
                            assert Video_Generation_Progress.text_content() == "Video generation is in progress"
                            print(Video_Generation_Progress.text_content())

                        with allure.step("Navigate to My Video Generation"):
                            logger.info("Navigating to My Video Generation")
                            Video_Generation = EditvideoGen.get_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                    print(video_generation_text)

                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"

                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

    @allure.title("PPT to video generate with speak note test")
    @allure.description("Video generate --> Download video from PPT generate with speak note ")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.VideoGen
    def test_PPT_to_video_speak_note_generate(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)
        EditvideoGen = EditvideoGenerate(page)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            memoryLeak.login_pictoryapp(self.script_email, self.script_password)

            logger.info("Clicking on Proceed button")
            videoGen.dynamicbar_invisible_scrolClick(PPTtoVideoLocators.Proceed_buton[1])

            EditvideoGen.get_uploadmp4_file("input[name='file'][type='file']", os.path.join('videoGen', 'Tips to start food business.pptx'))
            videoGen.get_speaker_note(EditVideoLocators.speak[1])
            EditvideoGen.background_click(EditVideoLocators.generate_vid[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

            if videoGen.is_elementvisible(ScriptToVideoLocators.branding[1]):
                logger.info("Applying brand on the video")

                EditvideoGen.scrollToclick_element(EditVideoLocators.edit_board[1])
                element = videoGen.get_apply_brand(ScriptToVideoLocators.branding[1])
                if element:
                    assert element.text_content() == "brand applied successfully", f"Expected 'brand applied successfully', but got '{element.text_content()}'"

                with allure.step("Speaker note on storyboard"):
                    logger.info("Speaker note on storyboard")
                    note = videoGen.get_speaker_note_apply(ScriptToVideoLocators.note_Story[1])
                    if note:
                        assert element.is_visible(), "The expected text 'start food business' is not visible."

                with allure.step("Apply Voiceover -->> Standard"):
                    logger.info("Applying voiceOver on the video")
                    voice_applied = videoGen.get_status_voiceover(ScriptToVideoLocators.Audio[1])
                    assert voice_applied.text_content() == "Applied"

                    videoGen.scrollToclick_element(ScriptToVideoLocators.WaterMarks[1])

                with allure.step("Apply layer -->> copyScene"):
                    logger.info("Applying layer -->> copyScene")
                    copyScene = videoGen.get_apply_layer_visual(ScriptToVideoLocators.Visual[1])
                    assert copyScene is not None, "Button not found on the page"
                    videoGen.get_delete_layer_visual(ScriptToVideoLocators.DeleteLayer[1])

                with allure.step("Get the final memory usage"):
                    final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                with allure.step("Navigate to the story Page"):
                    logger.info("Navigate to the story Page")
                    story_scene = videoGen.get_story_scene(ScriptToVideoLocators.scene1[1])
                    if story_scene:
                        assert story_scene.text_content() == "Scene 1"

                with allure.step("Apply transition the scene"):
                    logger.info("Apply transition the scene")
                    videoGen.get_transition_scene(ScriptToVideoLocators.transition[1])

                with allure.step("Navigate to the element Page"):
                    logger.info("Navigate to the element Page")
                    element_apply = videoGen.get_Element_apply(ScriptToVideoLocators.element_apply[1])
                    if element_apply:
                        assert element_apply.text_content() == "Element copied to all scenes.", f"Expected 'Element copied to all scenes', but got '{element.text_content()}'"

                    with allure.step("Navigate to the format Page"):
                        logger.info("Navigate to the format Page")
                        porTrait = videoGen.get_Format_apply(ScriptToVideoLocators.format[1])
                        if porTrait:
                            assert porTrait is not None, "Button not found on the page"

                            attribute = EditvideoGen.Attribute_name()
                            if attribute:
                                name = attribute.get_attribute("value")
                            else:
                                logger.error("Failed to retrieve the attribute name.")
                                assert False, "Attribute name not found."

                        with allure.step("Navigate to My Project Page"):
                            logger.info("Navigating to My Project Page")
                            Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    print(video_generation_text)
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"
                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

                            videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                        with allure.step("Check video element is present on Page"):
                            videoGen.is_videoscript_visible(name)

                        with allure.step("Check for memory leaks"):
                            memory_difference_mb = final_memory_usage - initial_memory_usage
                            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

                            print(f"{memory_difference_mb:.2f}:mb")
                            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                        with allure.step("Check video URL is present on Page"):
                            element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                            if element:
                                video = videoGen.is_url_exist_myvideos()
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("PPT to video generate test")
    @allure.description("Video generate --> Download video from PPT generate")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.VideoGen
    def test_PPT_to_video_generate(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)
        EditvideoGen = EditvideoGenerate(page)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            memoryLeak.login_pictoryapp(self.script_email, self.script_password)

            logger.info("Clicking on Proceed button")
            videoGen.dynamicbar_invisible_scrolClick(PPTtoVideoLocators.Proceed_buton[1])

            EditvideoGen.get_uploadmp4_file("input[name='file'][type='file']", os.path.join('videoGen', 'Tips to start food business.pptx'))
            EditvideoGen.background_click(EditVideoLocators.generate_vid[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

            if videoGen.is_elementvisible(ScriptToVideoLocators.branding[1]):
                logger.info("Applying brand on the video")

                EditvideoGen.scrollToclick_element(EditVideoLocators.edit_board[1])
                element = videoGen.get_apply_brand(ScriptToVideoLocators.branding[1])
                if element:
                    assert element.text_content() == "brand applied successfully", f"Expected 'brand applied successfully', but got '{element.text_content()}'"

                with allure.step("Apply Voiceover -->> Standard"):
                    logger.info("Applying voiceOver on the video")
                    voice_applied = videoGen.get_status_voiceover(ScriptToVideoLocators.Audio[1])
                    assert voice_applied.text_content() == "Applied"

                    videoGen.scrollToclick_element(ScriptToVideoLocators.WaterMarks[1])

                with allure.step("Apply layer -->> copyScene"):
                    logger.info("Applying layer -->> copyScene")
                    copyScene = videoGen.get_apply_layer_visual(ScriptToVideoLocators.Visual[1])
                    assert copyScene is not None, "Button not found on the page"
                    videoGen.get_delete_layer_visual(ScriptToVideoLocators.DeleteLayer[1])

                with allure.step("Get the final memory usage"):
                    final_memory_usage = MemoryUsage.log_memory_usage("Final ")

                with allure.step("Navigate to the story Page"):
                    logger.info("Navigate to the story Page")
                    story_scene = videoGen.get_story_scene(ScriptToVideoLocators.scene1[1])
                    if story_scene:
                        assert story_scene.text_content() == "Scene 1"

                with allure.step("Apply transition the scene"):
                    logger.info("Apply transition the scene")
                    videoGen.get_transition_scene(ScriptToVideoLocators.transition[1])

                with allure.step("Navigate to the element Page"):
                    logger.info("Navigate to the element Page")
                    element_apply = videoGen.get_Element_apply(ScriptToVideoLocators.element_apply[1])
                    if element_apply:
                        assert element_apply.text_content() == "Element copied to all scenes.", f"Expected 'Element copied to all scenes', but got '{element.text_content()}'"

                    with allure.step("Navigate to the format Page"):
                        logger.info("Navigate to the format Page")
                        porTrait = videoGen.get_Format_apply(ScriptToVideoLocators.format[1])
                        if porTrait:
                            assert porTrait is not None, "Button not found on the page"

                            attribute = EditvideoGen.Attribute_name()
                            if attribute:
                                name = attribute.get_attribute("value")
                            else:
                                logger.error("Failed to retrieve the attribute name.")
                                assert False, "Attribute name not found."

                        with allure.step("Navigate to My Project Page"):
                            logger.info("Navigating to My Project Page")
                            Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                            if Video_Generation:
                                video_generation_text = Video_Generation.text_content()
                                if "Video Generation is completed" in video_generation_text:
                                    print(video_generation_text)
                                    assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                                elif "Video Generation Failed" in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video Generation Failed"
                                elif "Video generation errored." in video_generation_text:
                                    print(video_generation_text)
                                    assert False, "Video generation errored"

                            videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                        with allure.step("Check video element is present on Page"):
                            videoGen.is_videoscript_visible(name)

                        with allure.step("Check for memory leaks"):
                            memory_difference_mb = final_memory_usage - initial_memory_usage
                            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

                            print(f"{memory_difference_mb:.2f}:mb")
                            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

                        with allure.step("Check video URL is present on Page"):
                            element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                            if element:
                                video = videoGen.is_url_exist_myvideos()
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("Download video and apply -- > Transition, Element,Custom, stock visual and images from EVUT generate test")
    @allure.description("Video generate -->Download video and apply -- > Transition, Element, Custom, stock visual and images Transition from EVUT generate")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_EVUT_autohighlight_defaultVO_dectext_coloroverlay_Transition_Element_Custom_stock_visual_img(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 6)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            name = "EVUT_autohighlight_defaultVO_dectext_coloroverlay_Transition_Element_Custom_stock_visual_img"
            memoryLeak.login_pictoryapp(script_email, script_password)

            videoGen.do_clickOperation(ScriptToVideoLocators.Recent_Project_EVUT[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

            logger.info("Go to the storyboard Page")
            videoGen.do_clickOperation(ScriptToVideoLocators.WaterMarks[1])

        with allure.step("click on visual Page"):
            videoGen.scrollToclick_element(ScriptToVideoLocators.Visual[1])

        with allure.step("Get the final memory usage"):
            final_memory_usage = MemoryUsage.log_memory_usage("Final ")

        with allure.step("Check for memory leaks"):
            memory_difference_mb = final_memory_usage - initial_memory_usage
            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

            print(f"{memory_difference_mb:.2f}:mb")
            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

            with allure.step("navigate to My Project Page"):
                logger.info("Navigating to My Project Page")
                Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                if Video_Generation:
                    video_generation_text = Video_Generation.text_content()
                    if "Video Generation is completed" in video_generation_text:
                        print(video_generation_text)
                        assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                    elif "Video Generation Failed" in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video Generation Failed"
                    elif "Video generation errored." in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video generation errored"

                videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                with allure.step("Check video URL is present on Page"):
                    if videoGen.is_videoscript_visible(name):
                        element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                        if element:
                            video = videoGen.is_url_exist_myvideos()
                            if video:
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("Download A2V_Image_fetch")
    @allure.description("Video generate -->Download A2V_Image_fetch")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_A2V_Image_fetch(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 8)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            name = "A2V_Image_fetch"
            memoryLeak.login_pictoryapp(script_email, script_password)

            videoGen.do_clickOperation(ScriptToVideoLocators.Recent_Project_A2v[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

            logger.info("Go to the storyboard Page")
            videoGen.do_clickOperation(ScriptToVideoLocators.WaterMarks[1])

        with allure.step("click on visual Page"):
            videoGen.scrollToclick_element(ScriptToVideoLocators.Visual[1])

        with allure.step("Get the final memory usage"):
            final_memory_usage = MemoryUsage.log_memory_usage("Final ")

        with allure.step("Check for memory leaks"):
            memory_difference_mb = final_memory_usage - initial_memory_usage
            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

            print(f"{memory_difference_mb:.2f}:mb")
            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

            with allure.step("navigate to My Project Page"):
                logger.info("Navigating to My Project Page")
                Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                if Video_Generation:
                    video_generation_text = Video_Generation.text_content()
                    if "Video Generation is completed" in video_generation_text:
                        print(video_generation_text)
                        assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                    elif "Video generation failed" in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video generation failed"
                    elif "Video generation errored." in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video generation errored"

                videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                with allure.step("Check video URL is present on Page"):
                    if videoGen.is_videoscript_visible(name):
                        element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                        if element:
                            video = videoGen.is_url_exist_myvideos()
                            if video:
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

    @allure.title("Download video and apply custom VO and decor text from Script to video generate test --> Long Video")
    @allure.description("Video generate -->Download video and and apply custom VO and decor text from Script to video generate--> Long Video")
    @allure.severity(allure.severity_level.CRITICAL)  # decorators class level
    @pytest.mark.VideoGen
    def test_scriptTo_video_LongVideo_customVO_text_coloroverlay_Transition_Element_Custom_stock_visual_imageshort(self, playwright_context_and_page):
        context, page = playwright_context_and_page
        memoryLeak = MemoryLeak(page)
        videoGen = scriptvideoGenerate(page)

        script_email, script_password = TestDataForProject.get_login_credential("ScriptToVideo", 8)

        with allure.step("Login to the Pictory app"):
            logger.info("Logging into Pictory")
            name = "scriptvideo_customVo_text_coloroverlay_Transition_Element_Custom_stock_visual_image"
            memoryLeak.login_pictoryapp(script_email, script_password)

            videoGen.do_clickOperation(ScriptToVideoLocators.Recent_Project_scriptvideo[1])

        with allure.step("Get the initial memory usage"):
            initial_memory_usage = MemoryUsage.log_memory_usage("Initial")

            logger.info("Go to the storyboard Page")
            videoGen.do_clickOperation(ScriptToVideoLocators.WaterMarks[1])

        with allure.step("click on visual Page"):
            videoGen.scrollToclick_element(ScriptToVideoLocators.Visual[1])

        with allure.step("Get the final memory usage"):
            final_memory_usage = MemoryUsage.log_memory_usage("Final ")

        with allure.step("Check for memory leaks"):
            memory_difference_mb = final_memory_usage - initial_memory_usage
            MemoryUsage.attach_memory_usage("Memory Usage Difference", memory_difference_mb)

            print(f"{memory_difference_mb:.2f}:mb")
            assert memory_difference_mb < 500, f"Memory leak detected! Initial: {final_memory_usage:.2f} MB, Final: {final_memory_usage:.2f} MB, Difference: {memory_difference_mb:.2f} MB"

            with allure.step("navigate to My Project Page"):
                logger.info("Navigating to My Project Page")
                Video_Generation = videoGen.get_Long_Video_Generation_element(ScriptToVideoLocators.Video_Generation[1])
                if Video_Generation:
                    video_generation_text = Video_Generation.text_content()
                    if "Video Generation is completed" in video_generation_text:
                        print(video_generation_text)
                        assert video_generation_text == "Video Generation is completed", f"Expected 'Video Generation is completed', but got '{video_generation_text}'"
                    elif "Video Generation Failed" in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video Generation Failed"
                    elif "Video generation errored." in video_generation_text:
                        print(video_generation_text)
                        assert False, "Video generation errored"

                videoGen.scrollToclick_element(ScriptToVideoLocators.Project[1])

                with allure.step("Check video URL is present on Page"):
                    if videoGen.is_videoscript_visible(name):
                        element = videoGen.dynamicbar_invisible(HomeLocators.loader[1])
                        if element:
                            video = videoGen.is_url_exist_myvideos()
                            if video:
                                video_src = video.get_attribute("src")
                                assert video_src, f"Video src attribute for '{video_src}' is empty."
                                print("Video URL:", video_src)

